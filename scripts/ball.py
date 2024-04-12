import pygame

class Ball:

    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color
        self.is_correct = False
        self.is_there = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)

