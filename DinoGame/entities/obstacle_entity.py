import pygame
import random
from ..utils.resource_loader import load_image

class Obstacle:
    cactus_images = [
        load_image("cactus.png" ,(30, 50)),
        load_image("cactus.png" ,(33, 55)),
        load_image("cactus.png" ,(36, 60)),
        load_image("cactus.png" ,(39, 65)),
        load_image("cactus.png" ,(42, 70)),
    ]
    strange_cactus_images = [
        load_image("cactus.png" ,(72, 72)),
        load_image("cactus.png" ,(45, 90)),
        load_image("cactus.png" ,(48, 80)),
    ]

    bird_img = load_image("bird.png", (50, 40))
    strange_bird_img = load_image("strange_bird.png", (50, 40))

    def __init__(self, speed, kind, ground_y):
        self.speed = speed
        self.type = kind
        self.ground_y = ground_y

        if self.type == "cactus":
            self.image = random.choice(Obstacle.cactus_images)
            self.width, self.height = self.image.get_size()
            self.y = self.ground_y - self.height
            self.x = 800 + random.randint(0, 300)

        elif self.type == "bird":
            self.image = Obstacle.bird_img
            self.width, self.height = self.image.get_size()
            self.x = 800 + random.randint(0, 300)
            r = random.random()
            if r < 0.25:
                self.y = 200 + random.randint(10, 25)
            elif r < 0.5:
                self.y = 200 + random.randint(35, 45)
            else:
                self.y = 200 + random.randint(55, 90)

        elif self.type == "strange_cactus":
            self.image = random.choice(Obstacle.strange_cactus_images)
            self.width, self.height = self.image.get_size()
            self.y = self.ground_y - self.height
            self.x = 800 + random.randint(0, 300)

        elif self.type == "strange_bird":
            self.image = Obstacle.strange_bird_img
            self.width, self.height = self.image.get_size()
            self.x = 800 + random.randint(0, 150)
            r = random.random()
            if r < 0.15:
                self.y = 200 + random.randint(10, 25)
            elif r < 0.35:
                self.y = 200 + random.randint(35, 45)
            else:
                self.y = 200 + random.randint(55, 90)
                            
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.rect.x -= self.speed
        return self.rect.right < 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
