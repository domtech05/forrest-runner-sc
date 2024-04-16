import pygame


class physicsEntity:

    def __init__(self, game, entityType, pos, size):  # pass in all variables and assign to attributes
        self.collisions = None
        self.game = game
        self.type = entityType
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

    def rect(self):
        rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])  # create rect around player to allow collisions
        return rect

    def update(self, tilemap, movement=(0, 0)):
        

        frameMovement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        # HANDLE HORIZONTAL MOVEMENT

        entityRect = self.rect()
        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):
                if frameMovement[0] > 0:
                    self.pos[0] = rect.left
                    self.collisions['right'] = True
                    self.velocity[1] = 0
                if frameMovement[0] < 0:
                    self.pos[0] = rect.right
                    self.collisions['left'] = True

        # HANDLE VERTICAL MOVEMENT

        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):
                if frameMovement[1] > 0:
                    self.pos[1] = rect.top - self.size[1] # Adjust position based on bottom of the entity
                    self.collisions['down'] = True
                elif frameMovement[1] < 0:
                    self.pos[1] = rect.bottom # Adjust position based on top of the entity
                    self.collisions['up'] = True
                self.velocity[1] = 0  # Reset vertical velocity

        # noinspection PyTypeChecker
        self.velocity[1] = min(5, self.velocity[1] + 0.1)  # take the lower of two numbers and apply it to velocity.
        # Ensures velocity cannot go over 5

        self.pos[0] += frameMovement[0]
        self.pos[1] += frameMovement[1]

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.rect()))
        scaledCharacter = pygame.transform.scale(self.game.assets['player'], self.size)
        screen.blit(scaledCharacter, self.pos)