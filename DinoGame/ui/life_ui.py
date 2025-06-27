import pygame

class LifeUI:
    def __init__(self, life_manager):
        self.life_manager = life_manager
        self.font = pygame.font.SysFont(None, 48)
        self.danger_flash = False
        self.last_flash_toggle = 0
        self.flash_interval = 400  # ms

    def draw(self, screen):
        lives = self.life_manager.get_lives()
        text = self.font.render(f"Lives x {lives}", True, (255, 0, 0))
        screen.blit(text, (10, 60))

        # 生命只剩1个时绘制闪烁危险边框
        if lives == 1:
            now = pygame.time.get_ticks()
            if now - self.last_flash_toggle > self.flash_interval:
                self.danger_flash = not self.danger_flash
                self.last_flash_toggle = now
            if self.danger_flash:
                border_color = (150, 0, 0)
                thickness = 50
                pygame.draw.rect(screen, border_color, (0, 0, 800, thickness))
                pygame.draw.rect(screen, border_color, (0, 0, thickness, 400))
                pygame.draw.rect(screen, border_color, (0, 400 - thickness, 800, thickness))
                pygame.draw.rect(screen, border_color, (800 - thickness, 0, thickness, 400))
