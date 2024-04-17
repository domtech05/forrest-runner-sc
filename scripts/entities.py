import pygame


class physicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        self.pos[0] += frame_movement[0]
        entityRect = self.rect()
        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):
                if frame_movement[0] > 0:
                    entityRect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entityRect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entityRect.x
        
        self.pos[1] += frame_movement[1]
        entityRect = self.rect()
        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):
                if frame_movement[1] > 0:
                    entityRect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entityRect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entityRect.y
        
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
            
    def render(self, screen):
        scaledCharacter = pygame.transform.scale(self.game.assets['player'], self.size)
        screen.blit(scaledCharacter, self.pos)