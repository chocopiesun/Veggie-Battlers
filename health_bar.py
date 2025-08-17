import pygame

pygame.init()

class HealthBar:
    def __init__(self, x, y, width, height, max_health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.max_health = max_health
        self.current_health = max_health

        self.red_health_bar = pygame.Rect(self.x, self.y, self.width, self.height)
        self.green_health_bar = pygame.Rect(self.x, self.y, self.width, self.height)
        self.green_health_bar.width = self.width * (self.current_health / self.max_health)           

    def update_health(self, current_health, x, y):
        self.current_health = current_health
        self.green_health_bar.width = self.width * (self.current_health / self.max_health)
        if self.current_health <= 0:
            self.current_health = 0
        self.x = x
        self.y = y
        self.green_health_bar.topleft = (self.x, self.y)
        self.red_health_bar.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.x - 4, self.y - 4, self.width + 8, self.height + 8))
        pygame.draw.rect(screen, (255, 0, 0), self.red_health_bar)
        pygame.draw.rect(screen, (0, 255, 0), self.green_health_bar)