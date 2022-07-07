# cloudmask for TOA data

def toa(image):
    qa = image.select('BQA')
    mask = qa.bitwiseAnd(1 << 4).eq(0);
    return image.updateMask(mask)


# cloudmask for SR data
def sr(image):
    qa = image.select('pixel_qa');
    mask = qa.bitwiseAnd(1 << 3) or qa.bitwiseAnd(1 << 5)
    return image.updateMask(mask.Not())
