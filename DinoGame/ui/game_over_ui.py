import pygame
import os

class GameOverBanner:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 56)
        self.small_font = pygame.font.SysFont(None, 28)
        self.restart_button = None
        self.menu_button = None
        self.exit_button = None
        self.final_score = 0
        self.high_score = self.load_high_score()

    def set_final_score(self, score):
        self.final_score = score
        if score > self.high_score:
            self.high_score = score
            self.save_high_score(score)

    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen_width, screen_height = screen.get_size()

        # 最终得分
        score_text = self.font.render(f"Your Score: {self.final_score}", True, (218, 165, 32))
        score_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 4))
        screen.blit(score_text, score_rect)

        # 历史最高分
        high_text = self.small_font.render(f"Best Score: {self.high_score}", True, (184, 134, 11))
        high_rect = high_text.get_rect(center=(screen_width // 2, score_rect.bottom + 30))
        screen.blit(high_text, high_rect)

        # 按钮文本
        restart_text = self.small_font.render("Restart", True, (0, 0, 0))
        menu_text = self.small_font.render("Main Menu", True, (0, 0, 0))
        exit_text = self.small_font.render("Exit", True, (0, 0, 0))

        btn_width = max(restart_text.get_width(), menu_text.get_width(), exit_text.get_width()) + 40
        btn_height = restart_text.get_height() + 20
        gap = 20

        center_x = screen_width // 2
        start_y = high_rect.bottom + 30

        # 三个按钮垂直排列
        self.restart_button = pygame.Rect(0, 0, btn_width, btn_height)
        self.restart_button.center = (center_x, start_y + btn_height // 2)

        self.menu_button = pygame.Rect(0, 0, btn_width, btn_height)
        self.menu_button.center = (center_x, self.restart_button.bottom + gap + btn_height // 2)

        self.exit_button = pygame.Rect(0, 0, btn_width, btn_height)
        self.exit_button.center = (center_x, self.menu_button.bottom + gap + btn_height // 2)

        # 绘制按钮
        pygame.draw.rect(screen, (0, 255, 0), self.restart_button)
        pygame.draw.rect(screen, (0, 200, 200), self.menu_button)
        pygame.draw.rect(screen, (200, 0, 0), self.exit_button)

        screen.blit(restart_text, restart_text.get_rect(center=self.restart_button.center))
        screen.blit(menu_text, menu_text.get_rect(center=self.menu_button.center))
        screen.blit(exit_text, exit_text.get_rect(center=self.exit_button.center))

    def check_buttons(self, pos):
        if self.restart_button and self.restart_button.collidepoint(pos):
            return "restart"
        if self.menu_button and self.menu_button.collidepoint(pos):
            return "menu"
        if self.exit_button and self.exit_button.collidepoint(pos):
            return "exit"
        return None

    def load_high_score(self):
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as f:
                try:
                    return int(f.read())
                except ValueError:
                    return 0
        return 0

    def save_high_score(self, score):
        with open("high_score.txt", "w") as f:
            f.write(str(score))
