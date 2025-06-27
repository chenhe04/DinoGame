import random
from ..entities.obstacle_entity import Obstacle  

def get_bird_chance(score):
    if score < 25:
        return 0
    elif score < 49: # score == 49的时候不再生成蝙蝠
        return 0.65
    elif score < 75:
        return 0
    elif score < 97: 
        return 0.65
    elif score == 97: # 固定97生成蝙蝠 98生成仙人掌 99生成血色蝙蝠衔接过场
        return 1
    elif score == 98: 
        return 0
    else:
        return 1.0
    
def get_min_gap(score):
    base_gap = 475
    min_gap = min(675, base_gap + score * 2)  
    return min_gap
    
def try_spawn_obstacle(obstacles, speed, score, ground_y):
    min_gap = get_min_gap(score)
    if not obstacles or (800 - obstacles[-1].rect.x) > min_gap:
        bird_chance = get_bird_chance(score)
        if  random.random() < bird_chance:
            if score < 99:
                kind = "bird" 
            else:
                kind = "strange_bird"
        else:
            if score < 50:
                kind = "cactus"
            else:
                kind = "strange_cactus" 
        obstacle = Obstacle(speed, kind, ground_y)
        obstacles.append(obstacle)
