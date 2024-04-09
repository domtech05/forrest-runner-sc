import pygame


class physicsEntity:

    def __init__(self, game, entityType, pos, size):  # pass in all variables and assign to attributes
        self.collisions = None
        self.game = game
        self.type = entityType
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0],
                           self.size[1])  # create rect around player to allow collisions

    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        frameMovement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        # HANDLE HORIZONTAL MOVEMENT
        self.pos[0] += frameMovement[0]
        entityRect = self.rect()
        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):
                if frameMovement[0] > 0:
                    self.pos[0] = rect.left - self.size[0]
                    self.collisions['right'] = True
                    self.velocity[1] = 0
                if frameMovement[0] < 0:
                    self.pos[0] = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entityRect.x

        # HANDLE VERTICAL MOVEMENT
        self.pos[1] += frameMovement[1]
        entityRect = self.rect()
        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):
                if frameMovement[1] > 0:
                    self.pos[1] = rect.top
                    self.collisions['down'] = True
                if frameMovement[1] < 0:
                    self.pos[1] = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entityRect.y

        # noinspection PyTypeChecker
        self.velocity[1] = min(5, self.velocity[1] + 0.1)  # take the lower of two numbers and apply it to velocity.
        # Ensures velocity cannot go over 5

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

    def render(self, screen):
        scaledCharacter = pygame.transform.scale(self.game.assets['player'], self.size)
        screen.blit(scaledCharacter, self.pos)
