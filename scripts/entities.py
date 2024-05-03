import pygame


class physicsEntity:
    def __init__(self, game, entityType, pos, size):
        self.game = game
        self.type = entityType
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0, 0)):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        frameMovement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frameMovement[0]
        entityRect = self.rect()
        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):
                if frameMovement[0] > 0:
                    entityRect.right = rect.left
                    self.collisions['right'] = True
                if frameMovement[0] < 0:
                    entityRect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entityRect.x

        self.pos[1] += frameMovement[1]
        entityRect = self.rect()
        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):
                if frameMovement[1] > 0:
                    entityRect.bottom = rect.top
                    self.collisions['down'] = True
                if frameMovement[1] < 0:
                    entityRect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entityRect.y

        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0




class player(physicsEntity):
    def __init__(self, game, pos, size):
        self.playerImage = pygame.image.load("ASSETS/Images/entities/character-idle.png")
        super().__init__(game, 'player', pos, size)
        self.jumps = 1


    def update(self, tilemap, movement=(0, 0)):
        super().update(tilemap, movement=movement)

        if self.collisions['down']:  # if player is colliding with a tile below, allow one jump to be made (acts to reset jump counter)
            self.jumps = 1

        if self.pos[1] > 250:


    def render(self, screen, offset=(0, 0)):
        scaledCharacter = pygame.transform.scale(self.playerImage, self.size)
        screen.blit(scaledCharacter, (self.pos[0] - offset[0], self.pos[1] - offset[1]))

    def jump(self):
        if self.jumps:  # if jumps = 0 this goes false so loop doesn't run, hence character cannot jump
            self.velocity[1] = -3  # edit velocity to move player up and 'jump'
            self.jumps -= 1  # take one from jump limit


class enemy(physicsEntity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'enemy', pos, size)
        self.enemyImage = pygame.image.load('ASSETS/Images/entities/enemyCharacter.png')
        self.movement = (0,0)

    def update(self, tilemap):
        super().update(tilemap, movement=self.movement)

    def render(self, screen, offset=(0, 0)):
        scaledCharacter = pygame.transform.scale(self.enemyImage, self.size)
        screen.blit(scaledCharacter, (self.pos[0] - offset[0], self.pos[1] - offset[1]))