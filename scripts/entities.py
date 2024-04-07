import pygame


class physicsEntity:

    def __init__(self, game, entityType, pos, size):  # pass in all variables and assign to attributes
        self.game = game
        self.type = entityType
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])  # create rect around player to allow collisions

    def update(self, tilemap, movement=(0, 0)):
        frameMovement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])  # calculate total movement for the frame

        self.pos[0] += frameMovement[0]  # Update X position based on frame movement variable defined above
        entityRect = self.rect()
        for rect in tilemap.physicsRectsAround(self.pos):
            if entityRect.colliderect(rect):  # if collision is detected run below code


        self.pos[1] += frameMovement[1]  # same as above but for Y coordinate

        # noinspection PyTypeChecker
        self.velocity[1] = min(5, self.velocity[1] + 0.1)  # take the lower of two numbers and apply it to velocity.
        # Ensures velocity cannot go over 5

    def render(self, screen):
        scaledCharacter = pygame.transform.scale(self.game.assets['player'], self.size)
        screen.blit(scaledCharacter, self.pos)
