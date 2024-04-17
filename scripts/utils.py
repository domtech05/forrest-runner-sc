import os
import pygame

baseImagePath = 'ASSETS/Images/'
def loadImage(path):
    img = pygame.image.load(baseImagePath + path).convert()
    return img


def bulkImageLoad(path):
    images = []
    for imgName in sorted(os.listdir(baseImagePath + path)):
        images.append(loadImage(path + '/' + imgName))
    return images
