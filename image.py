import cv2
import os
import numpy as np
from PIL import Image
from PIL import ImageOps

path = os.listdir("data/new")
for i in path:
    image = Image.open("data/new/"+i)
    '''
    if image.size[0] < 144 or image.size[1] < 144:
        image = image.resize((image.size[0]*2,image.size[1]*2))
        im = ImageOps.mirror(image)
        im.save("data/train/"+ i[0:-4] +"_mirror.png")
    else:
        im = ImageOps.mirror(image)
        im.save("data/train/"+ i[0:-4] +"_mirror.png")
    '''
    #im = ImageOps.flip(image)
    #im.save("data/train/"+ i[0:-4] +"_flip.png")
    mean = 0.0   # some constant
    std = 1.0    # some constant (standard deviation) 
    row,col,ch= image.size[1],image.size[0],3
    mean = 0
    var = 0.1
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    #noisy.save("data/train/"+ i[0:-4] +"_noise.png")
    cv2.imwrite("data/train/"+ i[0:-4] +"_noise.png",noisy)
