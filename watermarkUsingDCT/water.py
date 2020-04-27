# Importing necessary libraries...
import numpy as np
import pywt
import os
from PIL import Image
from scipy.fftpack import dct
from scipy.fftpack import idct
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings


# Get the image path for cover image and watermark image.
path = os.path.join(settings.BASE_DIR, "watermark\\media")
image = ""
watermark = ""

def convertImage(imageName, size,imName):
    img = Image.open(imageName).resize((size, size), 1)
    # Convert RGB image to gray scale
    img = img.convert('L')
    # Storing the gray scale image    
    img.save(os.path.join(path,'processedInputImage/' + imName))
    imageArray = np.array(img.getdata(), dtype=np.float).reshape((size, size))
    return imageArray


# Embed watermark into the cover image
def embedWatermark(watermarkArray, originalImage):
    watermarkArraySize = len(watermarkArray[0])
    watermarkFlat = watermarkArray.ravel()
    ind = 0

    for x in range (0, len(originalImage), 8):
        for y in range (0, len(originalImage), 8):
            if ind < len(watermarkFlat):
                subdct = originalImage[x:x+8, y:y+8]
                subdct[5][5] = watermarkFlat[ind]
                originalImage[x:x+8, y:y+8] = subdct
                ind+= 1
    return originalImage
      

# DCT transform on image, i.e. image array
def applyDCT(imageArray):
    size = len(imageArray[0])
    allSubdct = np.empty((size, size))
    for i in range (0, size, 8):
        for j in range (0, size, 8):
            subpixels = imageArray[i:i+8, j:j+8]
            subdct = dct(dct(subpixels.T, norm="ortho").T, norm="ortho")
            allSubdct[i:i+8, j:j+8] = subdct
    return allSubdct


def inverseDCT(allSubdct):
    size = len(allSubdct[0])
    allSubidct = np.empty((size, size))
    for i in range (0, size, 8):
        for j in range (0, size, 8):
            subidct = idct(idct(allSubdct[i:i+8, j:j+8].T, norm="ortho").T, norm="ortho")
            allSubidct[i:i+8, j:j+8] = subidct

    return allSubidct


def getWatermark(dctWatermarkedCoeff, watermarkSize):
    subwatermarks = []
    for x in range (0, len(dctWatermarkedCoeff), 8):
        for y in range (0, len(dctWatermarkedCoeff), 8):
            coeffSlice = dctWatermarkedCoeff[x:x+8, y:y+8]
            subwatermarks.append(coeffSlice[5][5])

    watermark = np.array(subwatermarks).reshape(watermarkSize, watermarkSize)
    return watermark


def recoverWatermark(imageArray, model='haar', level=1):
    coeffsWatermarkedImage=list(pywt.wavedec2(data = imageArray, wavelet = model, level = level))
    dctWatermarkedCoeff = applyDCT(coeffsWatermarkedImage[0])
    watermarkArray = getWatermark(dctWatermarkedCoeff, 128)
    watermarkArray =  np.uint8(watermarkArray)
    #Save result
    img = Image.fromarray(watermarkArray)
    img.save(os.path.join(path,'result/recoveredWatermark.jpg'))

def printImage(imageArray, name):
    imageArrayCopy = imageArray.clip(0, 255)
    imageArrayCopy = imageArrayCopy.astype("uint8")
    img = Image.fromarray(imageArrayCopy)
    img.save(os.path.join(path,'result/' + name))

def watermarkImage(img):
    global image
    global watermark
    image = os.path.join(path,'input\\1.jpg')
    watermark = os.path.join(path,'input\\2.jpg')
   
    model = 'haar'
    level = 1
    imageArray = convertImage(image, 2048,"1.jpg")
    watermarkArray = convertImage(watermark, 128,"2.jpg")
    coeffsImage = list(pywt.wavedec2(data=imageArray, wavelet = model, level = level))
    #coeffs_image = process_coefficients(image_array, model, level=level)
    dctArray = applyDCT(coeffsImage[0])
    dctArray = embedWatermark(watermarkArray, dctArray)
    coeffsImage[0] = inverseDCT(dctArray)
    # Watermark reconstruction
    imageArrayH=pywt.waverec2(coeffsImage, model)
    printImage(imageArrayH, 'watermarkedImage.jpg')
    # recover images
    recoverWatermark(imageArray = imageArrayH, model=model, level=level)


