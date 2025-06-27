import pygame

class ScoreManager:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 48)
        self.score = 0

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
