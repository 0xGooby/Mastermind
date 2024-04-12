import pygame

class Help:

    def __init__(self, y, color):
        self.color = color
        self.rect = pygame.Rect(470, y, 20, 30)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)