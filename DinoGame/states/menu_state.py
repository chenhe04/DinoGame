import pygame

def handle_menu_events(event, menu):
    if event.type == pygame.MOUSEBUTTONDOWN:
        action = menu.check_click(event.pos)
        return action
    return None

def draw_menu(screen, menu):
    menu.draw(screen)
