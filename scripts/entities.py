import pygame

class physicsEntity:
    def __init__(self, game, entityType, pos, size): # pass in all variables and assign to attributes
        self.game = game
        self.type = entityType
        self.pos = list(pos)
        self.size = size
        self.velocity = [0,0]

    def update(self, movement=(0, 0)):
        frameMovement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])  # calculate total movement for the frame

        self.velocity[1] = min(5, self.velocity[1] + 0.1) # take the lower of two numbers and apply it to velocity.
        # Ensures velocity cannot go over 5


        self.pos[0] += frameMovement[0]  # Update X position based on frame movement variable defined above
        self.pos[1] += frameMovement[1]  # same as above but for Y coordinate

    def render(self, screen):
        scaledCharacter = pygame.transform.scale(self.game.assets['player'], self.size)
        screen.blit(scaledCharacter, self.pos)