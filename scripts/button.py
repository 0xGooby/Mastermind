import pygame

class Button:

    def __init__(self, y, color):
        self.rect = pygame.Rect(420, y, 50, 20)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)