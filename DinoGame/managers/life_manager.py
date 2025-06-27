import pygame

class LifeManager:
    def __init__(self, lives=3):
        self.lives = lives
        self.invincible_until = 0
        self.last_hit_time = 0
        self.flash_duration = 1000  # 受伤后无敌闪烁时间(ms)

    def damage(self):
        now = pygame.time.get_ticks()
        if now > self.invincible_until:
            self.lives -= 1
            self.last_hit_time = now
            self.invincible_until = now + self.flash_duration
        return self.lives <= 0

    def is_invincible(self):
        return pygame.time.get_ticks() < self.invincible_until

    def should_draw_dino(self):
        now = pygame.time.get_ticks()
        if self.last_hit_time > 0 and now - self.last_hit_time < self.flash_duration:
            # 受伤闪烁效果，返回True表示绘制恐龙，False表示隐藏恐龙
            return (now // 100) % 2 == 1
        return True

    def get_lives(self):
        return self.lives
