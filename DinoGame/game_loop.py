import pygame
from .entities.dino_entity import Dino
from .managers.obstacle_manager import try_spawn_obstacle

def game_update_and_draw(screen, game_data, GROUND_Y):
    dino = game_data["dino"]
    obstacles = game_data["obstacles"]
    start_banner = game_data["start_banner"]
    score_manager = game_data["score_manager"]
    speed_manager = game_data["speed_manager"]
    milestone = game_data["milestone"]
    background = game_data["background"]
    life_manager = game_data["life_manager"]
    life_ui = game_data["life_ui"]
    game_over_banner = game_data["game_over_banner"]

    background.draw_background(screen)
    background.draw_ground(screen, GROUND_Y)

    if not game_data["game_over"]:
        dino.update()
        if life_manager.should_draw_dino():
            dino.draw(screen)

        try_spawn_obstacle(obstacles, speed_manager.get_speed(), score_manager.get_score(), GROUND_Y)

        for obstacle in list(obstacles):
            obstacle.speed = speed_manager.get_speed()
            if obstacle.update():
                obstacles.remove(obstacle)
                score_manager.increase_score()
                speed_manager.update_speed(score_manager.get_score())

                background.toggle_day_night(score_manager.get_score())
                milestone.check_and_trigger(score_manager.get_score())

            obstacle.draw(screen)

            if dino.get_rect().colliderect(obstacle.rect):
                if not life_manager.is_invincible():
                    obstacles.remove(obstacle)
                    game_data["game_over"] = life_manager.damage()
                    if game_data["game_over"]:
                        game_over_banner.set_final_score(score_manager.get_score())

    else:
        game_over_banner.draw(screen)

    score_manager.draw(screen)
    milestone.draw(screen)
    life_ui.draw(screen)

    if start_banner.draw(screen):
        return True
    return False
