import pygame
import random

class BackgroundManager:
    def __init__(self):
        self.is_day = True
        self.last_switch_score = 0
        self.ground_height = 100
        self.blood_moon_mode = False

    def toggle_day_night(self, score):
        if self.blood_moon_mode:
            return
    # 血月永久开启
        elif score >= 100:
            self.blood_moon_mode = True

        elif score % 25 == 0 and score != self.last_switch_score:
            self.is_day = not self.is_day
            self.last_switch_score = score

    def draw_background(self, screen):
        if self.blood_moon_mode:
            screen.fill((60, 20, 70))  # 深紫夜空
            self.draw_blood_moon(screen)
            self.draw_blood_stars(screen)
            self.draw_blood_clouds(screen)
        elif self.is_day:
            screen.fill((173, 216, 230))  # 白天背景
            self.draw_sun(screen)
            self.draw_clouds(screen)
        else:
            screen.fill((20, 24, 82))  # 夜晚背景
            self.draw_moon(screen)
            self.draw_stars(screen)

    def draw_ground(self, screen, ground_y):
        if self.blood_moon_mode:
            ground_color = (90, 20, 40)  # 深红土地
        elif self.is_day:
            ground_color = (50, 200, 50)  # 草地
        else:
            ground_color = (194, 178, 128)  # 沙地
        pygame.draw.rect(screen, ground_color, pygame.Rect(0, ground_y, screen.get_width(), self.ground_height))

    # ---------- 白天元素 ----------
    def draw_sun(self, screen):
        pygame.draw.circle(screen, (255, 204, 0), (750, 50), 30)

    def draw_clouds(self, screen):
        cloud_color = (235, 235, 235)
        cloud_sets = [((480, 70), 17), ((500, 65), 22), ((520, 70), 17),
                      ((250, 60), 15), ((270, 55), 20), ((290, 60), 15)]
        for pos, radius in cloud_sets:
            pygame.draw.circle(screen, cloud_color, pos, radius)

    # ---------- 夜晚元素 ----------
    def draw_moon(self, screen):
        pygame.draw.circle(screen, (240, 240, 220), (750, 50), 25)
        pygame.draw.circle(screen, (20, 24, 82), (740, 45), 20)

    def draw_stars(self, screen):
        for i in range(5):
            x = 100 + i * 120
            y = 60 + (i % 2) * 30
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 3)

    # ---------- 血月夜元素 ----------
    def draw_blood_moon(self, screen):
        # 主体血月
        pygame.draw.circle(screen, (200, 0, 0), (750, 60), 48)
        # 血蚀遮挡
        pygame.draw.circle(screen, (60, 20, 70), (735, 50), 30)

    def draw_blood_stars(self, screen):
        color = (200, 0, 0)
        star_positions = [(100 + i * 120, 60 + (i % 2) * 30) for i in range(5)]

        for x, y in star_positions:
            size = 12
            inner = 5  # 凹进去的程度

            points = [
                (x, y - size),                     # Top
                (x + inner, y - inner),            # Top-right inward
                (x + size, y),                     # Right
                (x + inner, y + inner),            # Bottom-right inward
                (x, y + size),                     # Bottom
                (x - inner, y + inner),            # Bottom-left inward
                (x - size, y),                     # Left
                (x - inner, y - inner)             # Top-left inward
            ]

            pygame.draw.polygon(screen, color, points)


    def draw_blood_clouds(self, screen):
        cloud_layers = [
            ((720, 80), 28, (120, 0, 0)),
            ((735, 85), 24, (160, 0, 0)),
            ((700, 92), 20, (140, 0, 0)),
            ((745, 90), 20, (180, 0, 0)),
        ]
        for pos, radius, color in cloud_layers:
            pygame.draw.circle(screen, color, pos, radius)
