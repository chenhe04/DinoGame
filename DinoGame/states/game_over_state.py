import pygame

def handle_game_over_events(event, game_over_banner):
    if event.type == pygame.MOUSEBUTTONDOWN:
        result = game_over_banner.check_buttons(event.pos)
        return result
    return None

def draw_game_over(screen, game_over_banner):
    game_over_banner.draw(screen)
