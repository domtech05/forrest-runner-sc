import random


class cloud:
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth  # Assign all attributes within the class
        
    def update(self):
        self.pos[0] += self.speed  # Update position based on cloud speed
        
    def render (self, screen, offset=(0, 0)):
        renderPos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)  # Create variable to assign a position to render the clouds at based on the camera offset
        screen.blit(self.img, (renderPos[0] % (screen.get_width() + self.img.get_width()) - self.img.get_width(), renderPos[1] % (screen.get_height() + self.img.get_height()) - self.img.get_height()))
        # render clouds to screen based on screen and image sizes
    

class clouds:  # class for cloud images and functions
    def __init__(self, cloudImages, count=16):
        self.clouds = []  # array for clouds
        
        for i in range(count):
            self.clouds.append(cloud((random.random() * 99999, random.random() * 99999), random.choice(cloudImages), random.random() * 0.05 + 0.05, random.random() * 0.6 + 0.2))
            # add clouds to array randomly
            
        self.clouds.sort(key=lambda x: x.depth)
        
    def update(self):
        for cloud in self.clouds:
            cloud.update()
            
    def render(self, screen, offset=(0, 0)):
        for cloud in self.clouds:
            cloud.render(screen, offset=offset)
            