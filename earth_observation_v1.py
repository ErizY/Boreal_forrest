########################################################
#                       IMPORTS                        #
#                                                      #
########################################################


import ast
import time
from dateutil.relativedelta import relativedelta
import lst.Landsat_LST as Landsat_LST # Land Surface Temperature package using Landsat satellite
import ee  # earth engine package to allow us to directly connect our drives together
from geetools import batch
import geemap.foliumap as geemap  # this package allows us to view and create an area of interest
               # and also this is one of the key packages we need
import pandas as pd  # this package allows us to read datasets and spreadsheets
import colorcet as cc
import matplotlib  # geometry and plotting package

def update_df(df, filename="wildfire_boreal_forest"):


    path = f'/content/drive/MyDrive/Data Science/Research/{filename}.csv'

    with open(path, 'w', encoding='utf-8-sig') as f:
        df.to_csv(f)


def maskS2clouds(image):
    qa = image.select('QA60');

    # Bits 10 and 11 are clouds and cirrus, respectively.
    cloudBitMask = 1 << 10
    cirrusBitMask = 1 << 11

    # Both flags should be set to zero, indicating clear conditions.
    mask = qa.bitwiseAnd(cloudBitMask).eq(0) and qa.bitwiseAnd(cirrusBitMask).eq(0)

    return image.updateMask(mask).divide(10000)


class Fire:
    def __init__(self, fire):
        self.df = pd.DataFrame(fire).T
        self.name = fire['name']
        self.country = fire.country
        self.area = fire.area
        self.area_type = fire.area_type
        self.region = fire.region_of_interest
        self.year = fire.year
        self.hectares = fire.area_hectares
        self.start_date = str((pd.to_datetime(fire.date_start, format='%d/%m/%Y')).date())
        self.end_date = str((pd.to_datetime(fire.date_end, format='%d/%m/%Y')).date())
        self.gee_coordinates = fire.gee_coordinates
        self.map_coordinates = ast.literal_eval(fire.map_coordinates)
        self.crs = fire.crs
        self.Map = geemap.Map(center=self.map_coordinates,
                                zoom=9,
                                Draw_export=False,
                                plugin_Draw=False)
        self.S5_params = None
        self.imageCollection = None
        self.gamma = None
        self.min = None
        self.max = None
        self.task = None

        self.Map.add_basemap("ROADMAP")

    def get_df(self):
        return self.df

    def get_gee_coordinates(self):
        if isinstance(self.gee_coordinates, ee.Geometry):
            return self.gee_coordinates
        elif isinstance(self.gee_coordinates, list):
            return ee.Geometry.Polygon(self.gee_coordinates)
        else:
            return ee.Geometry.Polygon(ast.literal_eval(self.gee_coordinates))

    def get_map_coordinates(self):
        return ast.literal_eval(self.map_coordinates)

    def set_end_date(self, years=0, months=0, days=0):
        self.end_date = str(
            (pd.to_datetime(self.start_date) + relativedelta(years=years, months=months, days=days)).date())

    def get_imagecollection(self, satellite, start_date=None, air_indice=None):

        if satellite == "S2":
            if start_date is not None:
                if pd.to_datetime(start_date) > pd.to_datetime('2017-03-28'):
                    self.imageCollection = ee.ImageCollection("COPERNICUS/S2_SR")
                else:
                    self.imageCollection = ee.ImageCollection("COPERNICUS/S2")
            else:
                if pd.to_datetime(self.start_date) > pd.to_datetime('2017-03-28'):
                    self.imageCollection = ee.ImageCollection("COPERNICUS/S2_SR")
                else:
                    self.imageCollection = ee.ImageCollection("COPERNICUS/S2")

        elif satellite == "S5":
            if start_date is not None:
                if pd.to_datetime(start_date) > pd.to_datetime('2017-11-13'):

                    if air_indice == 'co':
                        self.imageCollection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_CO').select(
                            'CO_column_number_density')
                        self.S5_params = {'min': 0, 'max': 0.05,
                                        'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']}
                    elif air_indice == 'no2':
                        self.imageCollection = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_NO2').select(
                            'tropospheric_NO2_column_number_density')
                        self.S5_params = {'min': 0, 'max': 0.0002,
                                        'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']}
                else:
                    raise ValueError('No data available before 13-11-2017 for Sentinel-5.')
            else:

                if pd.to_datetime(self.start_date) > pd.to_datetime('2017-11-13'):

                    if air_indice == 'co':
                        self.imageCollection = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_CO').select(
                            'CO_column_number_density')
                        self.S5_params = {'min': 0, 'max': 0.05,
                                        'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']}
                    elif air_indice == 'no2':
                        self.imageCollection = ee.ImageCollection('COPERNICUS/S5P/OFFL/L3_NO2').select(
                            'tropospheric_NO2_column_number_density')
                        self.S5_params = {'min': 0, 'max': 0.0002,
                                        'palette': ['black', 'blue', 'purple', 'cyan', 'green', 'yellow', 'red']}
                else:
                    raise ValueError('No data available before 13-11-2017 for Sentinel-5.')

    def update_coor(self, new_coord=None):

        if new_coord is not None:
            self.df.at[self.df.index[0], 'gee_coordinates'] = new_coord
            self.gee_coordinates = new_coord

        elif self.Map.draw_last_feature is not None:
            new_coordinates = self.Map.draw_last_feature.geometry().getInfo()['coordinates'][0]
            self.df.at[self.df.index[0], 'gee_coordinates'] = new_coordinates
            self.gee_coordinates = new_coordinates

        else:
            raise ValueError('You need to draw a shape on the map.')

    def get_tasks(self):
        # while ee.batch.Task.list()[0].status()['state'] != "COMPLETED":
        #     tasks = ee.batch.Task.list()
        #     print(tasks)
        #     time.sleep(5)
        return ee.batch.Task.list()[0].status()['state']

    def __get_images(self, satellite, start_date, end_date, cloudy_percentage=None, mask_clouds=False, min=None,
                     max=None, gamma=None, air_indice=None):

        self.get_imagecollection(satellite, start_date=start_date, air_indice=air_indice)
        self.gamma = gamma
        self.min = min
        self.max = max

        if mask_clouds:
            if (start_date is not None) and (end_date is not None):
                images = self.imageCollection.filterDate(start_date, end_date).filter(
                    ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', cloudy_percentage)).map(maskS2clouds)
                return images
            elif self.end_date is not None:
                images = self.imageCollection.filterDate(self.start_date, self.end_date).filter(
                    ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', cloudy_percentage)).map(maskS2clouds)
                return images
            else:
                raise ValueError(
                    'You need to add an end date with the .set_end_date(years, months, days) method.'
                    'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')

        elif cloudy_percentage:
            if (start_date is not None) and (end_date is not None):
                images = self.imageCollection.filterDate(start_date, end_date).filter(
                    ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', cloudy_percentage))
                return images
            elif self.end_date is not None:
                images = self.imageCollection.filterDate(self.start_date, self.end_date).filter(
                    ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', cloudy_percentage))
                return images
            else:
                raise ValueError(
                    'You need to add an end date with the .set_end_date(years, months, days) method.'
                    'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')
        else:
            if (start_date is not None) and (end_date is not None):
                images = self.imageCollection.filterDate(start_date, end_date)
                return images
            elif self.end_date is not None:
                images = self.imageCollection.filterDate(self.start_date, self.end_date)
                return images
            else:
                raise ValueError(
                    'You need to add an end date with the .set_end_date(years, months, days) method.'
                    'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')

    ########################################################
    #                LAYERS AVAILABLE                      #
    #                                                      #
    ########################################################

    def true_color(self, cloudy_percentage=50, gamma=1, min=0, max=1800, start_date=None, end_date=None):
        """
        The true_color() function plot image collection got from Google Earth Engine with the true color.

        :param cloudy_percentage: max percentage of clouds in the image
        :param gamma:
        :param min:
        :param max:
        :param max:
        :param max:
        :return: the images displayed on the map
        """
        satellite = "S2"
        images = self.__get_images(satellite, start_date, end_date, cloudy_percentage, min=min, max=max, gamma=gamma)

        self.Map.addLayer(images.median(), {'bands': ['B4', 'B3', 'B2'], 'min': self.min,
                                            'max': self.max, 'gamma': self.gamma}, "TRUE COLOR", True, 1)
        #self.Map.centerObject(self.get_gee_coordinates())

    def false_color(self, cloudy_percentage=50, gamma=1, min=0, max=3000, start_date=None, end_date=None):

        satellite = "S2"
        images = self.__get_images(satellite, start_date, end_date, cloudy_percentage, min=min, max=max, gamma=gamma)

        self.Map.addLayer(images.median(), {'bands': ["B8", "B4", "B3"], 'min': self.min,
                                            'max': self.max, 'gamma': self.gamma}, "FALSE COLOR", True, 1)
        # self.Map.centerObject(self.get_gee_coordinates())

    def swir(self, cloudy_percentage=50, gamma=1, min=0, max=3000, start_date=None, end_date=None):

        satellite = "S2"
        images = self.__get_images(satellite, start_date, end_date, cloudy_percentage, min=min, max=max, gamma=gamma)

        self.Map.addLayer(images.median(), {'bands': ["B12", "B8A", "B4"], 'min': self.min,
                                            'max': self.max, 'gamma': self.gamma}, "SWIR", True, 1)
        #self.Map.centerObject(self.get_gee_coordinates())

    def nbr(self, cloudy_percentage=50, start_date=None, end_date=None):

        def preprocessing(image):
            return ee.Image(image.expression(
                '(NIR-SWIR)/(NIR+SWIR)', {
                    'NIR': image.select('B8'),
                    'SWIR': image.select('B11'),
                }))

        satellite = "S2"
        images = self.__get_images(satellite, start_date, end_date, cloudy_percentage, mask_clouds=True)

        images = images.map(preprocessing)

        self.Map.addLayer(images.median(), {'min': -1, 'max': 1, 'palette': ['red', 'white', 'green']}, "NBR", True, 1)
        #self.Map.centerObject(self.get_gee_coordinates())

    def bai(self, cloudy_percentage=50, start_date=None, end_date=None):

        def preprocessing(image):
            return ee.Image(image.expression(
                '(1 - ((R2*R4*R4)/(R4))**(0.5))*((SWIR2 - R4)/((SWIR2 + R4)**(0.5)) + 1)', {
                    'RED': image.select('B4'),
                    'R2': image.select('B6'),
                    'R3': image.select('B7'),
                    'SWIR2': image.select('B12'),
                    'R4': image.select('B8A'),
                }))

        satellite = "S2"
        images = self.__get_images(satellite, start_date, end_date, cloudy_percentage, mask_clouds=True)

        images = images.map(preprocessing)

        self.Map.addLayer(images.median(), {'min': 0.0, 'max': 1.0, 'palette': cc.fire}, "BAI", True, 1)
        #self.Map.centerObject(self.get_gee_coordinates())

    def evi(self, cloudy_percentage=50, start_date=None, end_date=None):

        def preprocessing(image):
            return ee.Image(image.expression(
                '(2.5 * (B08 - B04)) / ((B08 + 6.0 * B04 - 7.5 * B02) + 1.0)', {
                    'B08': image.select('B8'),
                    'B04': image.select('B4'),
                    'B02': image.select('B2'),
                }))

        satellite = "S2"
        images = self.__get_images(satellite, start_date, end_date, cloudy_percentage, mask_clouds=True)

        images = images.map(preprocessing)

        self.Map.addLayer(images.median(), {'min': 0.0, 'max': 1.0,
                                          'palette': [matplotlib.colors.rgb2hex(matplotlib.cm.get_cmap("YlGn")(i))
                                                      for i in range(matplotlib.cm.get_cmap("YlGn").N)]}, 'EVI',
                          True, 1)
        #self.Map.centerObject(self.get_gee_coordinates())

    def air_quality(self, air_indice, start_date=None, end_date=None):

        satellite = "S5"
        images = self.__get_images(satellite, start_date, end_date, air_indice=air_indice)

        self.Map.addLayer(images.max(), self.S5_params, 'S5', True, 1)
        self.Map.centerObject(self.get_gee_coordinates())

    def lst(self, start_date=None, end_date=None):

        if (start_date is not None) and (end_date is not None):
            images = Landsat_LST.collection('L8', start_date, end_date, self.get_gee_coordinates(),
                                            use_ndvi=True).max()
        elif self.end_date is not None:
            # get landsat collection with added variables: NDVI, FVC, TPW, EM, LST
            images = Landsat_LST.collection('L8', self.start_date, self.end_date, self.get_gee_coordinates(),
                                            use_ndvi=True).max()
        else:
            raise ValueError(
                'You need to add an end date with the .set_end_date(years, months, days) method.'
                'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')

        cmap1 = ['blue', 'cyan', 'green', 'yellow', 'red']
        cmap2 = ['F2F2F2', 'EFC2B3', 'ECB176', 'E9BD3A', 'E6E600', '63C600', '00A600']

        # self.Map.addLayer(images.select('TPW'), {'min':0.0, 'max':60.0, 'palette':cmap1},'TCWV', True, 1)
        # self.Map.addLayer(images.select('TPWpos'), {'min':0.0, 'max':9.0, 'palette':cmap1},'TCWVpos', True, 1)
        # self.Map.addLayer(images.select('FVC'), {'min':0.0, 'max':1.0, 'palette':cmap2}, 'FVC', True, 1)
        # self.Map.addLayer(images.select('EM'), {'min':0.9, 'max':1.0, 'palette':cmap1}, 'Emissivity', True, 1)
        # self.Map.addLayer(images.select('B10'), {'min':290, 'max':320, 'palette':cmap1}, 'TIR BT', True, 1)
        # self.Map.addLayer(LandsatColl.select('LST'), {'min':290, 'max':320, 'palette':cmap1}, 'LST', True, 1)

        if len(images.getInfo()["bands"])>0:
            self.Map.addLayer(images.select('LST'), {'min': 290, 'max': 320, 'palette': cmap1}, 'LST', True, 1)
        #self.Map.centerObject(self.get_gee_coordinates())

    ########################################################
    #                   EXPORT IMAGES                      #
    #                                                      #
    ########################################################

    def get_task_export(self, image, folder, scale, layer, start_date):

        return ee.batch.Export.image.toDrive(
            image=image,
            folder=folder,
            scale=scale,
            maxPixels=1e13,
            crs=self.crs,
            region=self.get_gee_coordinates(),
            description=f"{start_date}-{layer}",
        )

    def export(self, folder, layer, start_date=None, end_date=None, scale=10):
        """
        Export the images selected through layers available to Google Drive.

        :param folder: name of folder in Google Drive (no need to give the all path, the function will find the right folder even if it is a subfolder).
        :param layer: name of layer available.
        :param start_date: the start date of the range date.
        :param end_date: the end date of the range date.
        :param scale: the resolution of the image to export (lower is the number higher is the resolution according to the satellite capacities).
        :return: None
        """

        # List of layers available:
        # "true" : to export the image with true colors

        if layer == 'true':

            # if start_date and end_date optional parameters are used
            if (start_date is not None) and (end_date is not None):

                image = self.imageCollection.filterDate(start_date, end_date).filterBounds(
                    self.get_gee_coordinates()).median().visualize(bands=['B4', 'B3', 'B2'], gamma=self.gamma,
                                                                 min=self.min, max=self.max)
                self.task = self.get_task_export(image, folder, scale, layer, start_date)
                self.task.start()

            # if start_date of the dataset and set_end_date() function are used
            elif self.end_date is not None:
                image = self.imageCollection.filterDate(self.start_date, self.end_date).filterBounds(
                    self.get_gee_coordinates()).median().visualize(bands=['B4', 'B3', 'B2'], gamma=self.gamma,
                                                                 min=self.min, max=self.max)
                self.task = self.get_task_export(image, folder, scale, layer, self.start_date)
                self.task.start()

            else:
                raise ValueError(
                    'You need to add an end date with the .set_end_date(years, months, days) method.'
                    'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')

        elif layer == 'false':

            # if start_date and end_date optional parameters are used
            if (start_date is not None) and (end_date is not None):

                image = self.imageCollection.filterDate(start_date, end_date).filterBounds(
                    self.get_gee_coordinates()).median().visualize(bands=["B8", "B4", "B3"], gamma=self.gamma,
                                                                 min=self.min, max=self.max)
                self.task = self.get_task_export(image, folder, scale, layer, start_date)
                self.task.start()

            # if start_date of the dataset and set_end_date() function are used
            elif self.end_date is not None:

                image = self.imageCollection.filterDate(self.start_date, self.end_date).filterBounds(
                    self.get_gee_coordinates()).median().visualize(bands=["B8", "B4", "B3"], gamma=self.gamma,
                                                                 min=self.min, max=self.max)
                self.task = self.get_task_export(image, folder, scale, layer, self.start_date)
                self.task.start()

            else:
                raise ValueError(
                    'You need to add an end date with the .set_end_date(years, months, days) method.'
                    'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')

        elif layer == 'swir':

            # if start_date and end_date optional parameters are used
            if (start_date is not None) and (end_date is not None):
                image = self.imageCollection.filterDate(start_date, end_date).filterBounds(
                    self.get_gee_coordinates()).median().visualize(bands=["B12", "B8A", "B4"], gamma=self.gamma,
                                                                 min=self.min, max=self.max)
                self.task = self.get_task_export(image, folder, scale, layer, start_date)
                self.task.start()

            # if start_date of the dataset and set_end_date() function are used
            elif self.end_date is not None:

                image = self.imageCollection.filterDate(self.start_date, self.end_date).filterBounds(
                    self.get_gee_coordinates()).median().visualize(bands=["B12", "B8A", "B4"], gamma=self.gamma,
                                                                 min=self.min, max=self.max)
                self.task = self.get_task_export(image, folder, scale, layer, self.start_date)
                self.task.start()

            else:
                raise ValueError(
                    'You need to add an end date with the .set_end_date(years, months, days) method.'
                    'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')

        elif layer == "bai":

            # if start_date and end_date optional parameters are used
            if (start_date is not None) and (end_date is not None):

                image = self.imageCollection.filterDate(start_date, end_date).filterBounds(
                    self.get_gee_coordinates()).map(lambda image: ee.Image(image.expression(
                    '(2.5 * (B08 - B04)) / ((B08 + 6.0 * B04 - 7.5 * B02) + 1.0)', {
                        'B08': image.select('B8'),
                        'B04': image.select('B4'),
                        'B02': image.select('B2'),
                    }))).median().visualize(min=0.0, max=1.0, palette=cc.fire)
                self.task = self.get_task_export(image, folder, scale, layer, start_date)
                self.task.start()

            # if start_date of the dataset and set_end_date() function are used
            elif self.end_date is not None:

                image = self.imageCollection.filterDate(self.start_date, self.end_date).filterBounds(
                    self.get_gee_coordinates()).map(lambda image: ee.Image(image.expression(
                    '(2.5 * (B08 - B04)) / ((B08 + 6.0 * B04 - 7.5 * B02) + 1.0)', {
                        'B08': image.select('B8'),
                        'B04': image.select('B4'),
                        'B02': image.select('B2'),
                    }))).median().visualize(min=0.0, max=1.0, palette=cc.fire)
                self.task = self.get_task_export(image, folder, scale, layer, self.start_date)
                self.task.start()

            else:
                raise ValueError(
                    'You need to add an end date with the .set_end_date(years, months, days) method.'
                    'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')

        elif layer == "nbr":

            # if start_date and end_date optional parameters are used
            if (start_date is not None) and (end_date is not None):

                image = self.imageCollection.filterDate(start_date, end_date).filterBounds(
                    self.get_gee_coordinates()).map(lambda image: ee.Image(image.expression(
                    '(2.5 * (B08 - B04)) / ((B08 + 6.0 * B04 - 7.5 * B02) + 1.0)', {
                        'B08': image.select('B8'),
                        'B04': image.select('B4'),
                        'B02': image.select('B2'),
                    }))).median().visualize(min=-1, max=1, palette=['red', 'white', 'green'])
                self.task = self.get_task_export(image, folder, scale, layer, start_date)
                self.task.start()

            # if start_date of the dataset and set_end_date() function are used
            elif self.end_date is not None:

                image = self.imageCollection.filterDate(self.start_date, self.end_date).filterBounds(
                    self.get_gee_coordinates()).map(lambda image: ee.Image(image.expression(
                    '(2.5 * (B08 - B04)) / ((B08 + 6.0 * B04 - 7.5 * B02) + 1.0)', {
                        'B08': image.select('B8'),
                        'B04': image.select('B4'),
                        'B02': image.select('B2'),
                    }))).median().visualize(min=-1, max=1, palette=['red', 'white', 'green'])
                self.task = self.get_task_export(image, folder, scale, layer, self.start_date)
                self.task.start()

            else:
                raise ValueError(
                    'You need to add an end date with the .set_end_date(years, months, days) method.'
                    'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')

        elif layer == "evi":

            # if start_date and end_date optional parameters are used
            if (start_date is not None) and (end_date is not None):

                image = self.imageCollection.filterDate(start_date, end_date).filterBounds(
                    self.get_gee_coordinates()).map(lambda image: ee.Image(image.expression(
                    '(NIR-SWIR)/(NIR+SWIR)', {
                        'NIR': image.select('B8'),
                        'SWIR': image.select('B11'),
                    }))).median().visualize(min=0.0, max=1.0, palette=[
                    matplotlib.colors.rgb2hex(matplotlib.cm.get_cmap("YlGn")(i)) for i in
                    range(matplotlib.cm.get_cmap("YlGn").N)])
                self.task = self.get_task_export(image, folder, scale, layer, start_date)
                self.task.start()

            # if start_date of the dataset and set_end_date() function are used
            elif self.end_date is not None:

                image = self.imageCollection.filterDate(self.start_date, self.end_date).filterBounds(
                    self.get_gee_coordinates()).map(lambda image: ee.Image(image.expression(
                    '(NIR-SWIR)/(NIR+SWIR)', {
                        'NIR': image.select('B8'),
                        'SWIR': image.select('B11'),
                    }))).median().visualize(min=0.0, max=1.0, palette=[
                    matplotlib.colors.rgb2hex(matplotlib.cm.get_cmap("YlGn")(i)) for i in
                    range(matplotlib.cm.get_cmap("YlGn").N)])
                self.task = self.get_task_export(image, folder, scale, layer, self.start_date)
                self.task.start()

            else:
                raise ValueError(
                    'You need to add an end date with the .set_end_date(years, months, days) method.'
                    'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')

        elif layer == "lst":

            # if start_date and end_date optional parameters are used
            if (start_date is not None) and (end_date is not None):

                image = Landsat_LST.collection('L8', start_date, end_date, self.get_gee_coordinates(),
                                               use_ndvi=True).filterBounds(
                    self.get_gee_coordinates()).median().visualize(min=290, max=320, palette=['blue', 'cyan', 'green',
                                                                                            'yellow', 'red'])
                self.task = self.get_task_export(image, folder, scale, layer, start_date)
                self.task.start()

            # if start_date of the dataset and set_end_date() function are used
            elif self.end_date is not None:

                image = Landsat_LST.collection('L8', self.start_date, self.end_date, self.get_gee_coordinates(),
                                               use_ndvi=True).filterBounds(
                    self.get_gee_coordinates()).median().visualize(min=290, max=320, palette=['blue', 'cyan', 'green',
                                                                                            'yellow', 'red'])
                self.task = self.get_task_export(image, folder, scale, layer, self.start_date)
                self.task.start()

            else:
                raise ValueError(
                    'You need to add an end date with the .set_end_date(years, months, days) method.'
                    'Or to use start_date=YYYY-MM-DD and end_date=YYYY-MM-DD parameters.')

        else:
            raise ValueError(
                'You need to give a value for the layer parameter among: true, false, swir, nbr, bai, evi and lst')
