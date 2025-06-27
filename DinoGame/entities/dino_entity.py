import pygame
from ..utils.resource_loader import load_image

class Dino:
    def __init__(self, ground_y):
        self.image = load_image("dino.png", (60, 60))  
        self.width, self.height = self.image.get_size()  
        self.x = 100
        self.y = ground_y
        self.ground_y = ground_y
        self.vel_y = 0
        self.jump_force = -15
        self.gravity = 1
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.vel_y = self.jump_force
            self.is_jumping = True

    def update(self):
        self.y += self.vel_y
        self.vel_y += self.gravity
        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.is_jumping = False

    def draw(self, screen):
        # 自动用宽高来偏移绘制
        screen.blit(self.image, (self.x - self.width // 2, self.y - self.height))

    def get_rect(self):
        # 自动用宽高来生成矩形
        return pygame.Rect(self.x - self.width // 2, self.y - self.height, self.width, self.height)

