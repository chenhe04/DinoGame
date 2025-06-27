import pygame

class MilestoneBanner:
    def __init__(self):
        self.last_milestone = 0
        self.show_time = 0       
        self.duration = 1000     
        self.color1 = (0, 200, 0)
        self.color2 = (255, 215, 0)
        self.flash_interval = 100
        self.font = pygame.font.SysFont(None, 48)

    def check_and_trigger(self, score):
        if score != 0 and score % 10 == 0 and score != self.last_milestone:
            self.last_milestone = score
            self.show_time = pygame.time.get_ticks()

    def draw(self, screen):
        if self.last_milestone == 0:
            return  # 没有触发过则不画

        current_time = pygame.time.get_ticks()
        elapsed = current_time - self.show_time

        if elapsed < self.duration:
            flash_phase = ((current_time // self.flash_interval) % 2) == 0
            color = self.color1 if flash_phase else self.color2
            text = self.font.render(f"Great! You reached {self.last_milestone} points!", True, color)
            rect = text.get_rect(center=(400, 200))
            screen.blit(text, rect)
