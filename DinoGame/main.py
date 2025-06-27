import pygame
from .ui.menu_ui import MainMenu
from .ui.game_over_ui import GameOverBanner
from .ui.start_ui import StartBanner
from .ui.milestone_ui import MilestoneBanner
from .ui.background_ui import BackgroundManager
from .ui.life_ui import LifeUI

from .entities.dino_entity import Dino
from .managers.score_manager import ScoreManager
from .managers.speed_manager import SpeedManager  
from .managers.life_manager import LifeManager

from .states import menu_state, game_over_state
from .game_loop import game_update_and_draw

GROUND_Y = 350

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption("Dino Game ver.1.0.1 Made by CHEN He")
    return screen

def create_game_data(game_over_banner):
    life_manager = LifeManager(lives=3)
    speed_manager = SpeedManager()  
    return {
        "dino": Dino(GROUND_Y),
        "obstacles": [],
        "start_banner": StartBanner(),
        "score_manager": ScoreManager(),
        "speed_manager": speed_manager,           
        "milestone": MilestoneBanner(),
        "background": BackgroundManager(),
        "life_manager": life_manager,
        "life_ui": LifeUI(life_manager),
        "game_over_banner": game_over_banner,
        "game_over": False,
    }

def main():
    screen = init_game()
    clock = pygame.time.Clock()

    menu = MainMenu()
    game_over_banner = GameOverBanner()
    state = "MENU"
    running = True
    game_data = {}

    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif state == "MENU":
                action = menu_state.handle_menu_events(event, menu)
                if action == "start":
                    game_data = create_game_data(game_over_banner)
                    state = "PLAYING"
                elif action == "exit":
                    running = False

            elif state == "PLAYING":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not game_data["game_over"]:
                        game_data["dino"].jump()

            elif state == "GAME_OVER":
                result = game_over_state.handle_game_over_events(event, game_over_banner)
                if result == "restart":
                    game_data = create_game_data(game_over_banner)
                    state = "PLAYING"
                elif result == "menu":
                    state = "MENU"
                elif result == "exit":
                    running = False

        if state == "MENU":
            menu_state.draw_menu(screen, menu)

        elif state == "PLAYING":
            waiting_to_start = game_update_and_draw(screen, game_data, GROUND_Y)
            if game_data["game_over"]:
                state = "GAME_OVER"

        elif state == "GAME_OVER":
            game_over_state.draw_game_over(screen, game_over_banner)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
