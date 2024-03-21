import pygame

basePath = 'ASSETS/Images/'
def loadImage(path):
    img = pygame.image.load(basePath + path)
    return img