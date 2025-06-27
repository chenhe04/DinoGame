import pygame

class MainMenu:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 64)
        self.small_font = pygame.font.SysFont(None, 32)
        # 两个按钮宽高
        button_width, button_height = 150, 60
        screen_width = 800
        
        # 两个按钮居中且有垂直间隔
        center_x = screen_width // 2
        start_y = 250
        gap = 20
        
        self.start_button_rect = pygame.Rect(0, 0, button_width, button_height)
        self.start_button_rect.center = (center_x, start_y)
        
        self.exit_button_rect = pygame.Rect(0, 0, button_width, button_height)
        self.exit_button_rect.center = (center_x, start_y + button_height + gap)

    def draw(self, screen):
        screen.fill((250, 240, 230))
        title = self.font.render("Welcome to Dino Game!!", True, (0, 0, 0))
        title_rect = title.get_rect(center=(screen.get_width() // 2, 150))
        screen.blit(title, title_rect)

        version_text = self.small_font.render("ver.1.0.1", True, (100, 100, 100))
        version_rect = version_text.get_rect(center=(screen.get_width() // 2, title_rect.bottom + 10))
        screen.blit(version_text, version_rect)

        # 画开始按钮
        pygame.draw.rect(screen, (0, 150, 0), self.start_button_rect)
        start_text = self.font.render("Start", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=self.start_button_rect.center)
        screen.blit(start_text, start_text_rect)

        # 画退出按钮
        pygame.draw.rect(screen, (200, 0, 0), self.exit_button_rect)
        exit_text = self.font.render("Exit", True, (255, 255, 255))
        exit_text_rect = exit_text.get_rect(center=self.exit_button_rect.center)
        screen.blit(exit_text, exit_text_rect)

    def check_click(self, pos):
        if self.start_button_rect.collidepoint(pos):
            return "start"
        elif self.exit_button_rect.collidepoint(pos):
            return "exit"
        else:
            return None
