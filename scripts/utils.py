import pygame

basePath = 'ASSETS/Images/'
def load_image(path):
    img = pygame.image.load(basePath + path)
    return img