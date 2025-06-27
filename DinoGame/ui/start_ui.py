import pygame

class StartBanner:
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.duration = 1000  
        self.color1 = (0, 200, 0)
        self.color2 = (255, 215, 0)
        self.flash_interval = 100
        self.font = pygame.font.SysFont(None, 48)
        self.active = True

    def draw(self, screen):
        if not self.active:
            return False

        current_time = pygame.time.get_ticks()
        elapsed = current_time - self.start_time
        if elapsed < self.duration:
            flash_phase = ((current_time // self.flash_interval) % 4) == 0
            color = self.color1 if flash_phase else self.color2
            text = self.font.render("Let's Go!", True, color)
            rect = text.get_rect(center=(400, 200))
            screen.blit(text, rect)
            return True
        else:
            self.active = False
            return False
