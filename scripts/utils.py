import os

import pygame

basePath = 'ASSETS/Images/'
def loadImage(path):
    img = pygame.image.load(basePath + path)
    return img

def bulkImageLoad(path):
    images = []
    for imgName in sorted(os.listdir(basePath + path)):
        images.append(loadImage(path + '/' + imgName))
    return images
