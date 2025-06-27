import os
import sys
import pygame

def resource_path(relative_path):
    try:
        # PyInstaller 解压时的临时目录
        base_path = sys._MEIPASS
    except AttributeError:
        # 开发环境，当前文件的上两级目录
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, "assets", relative_path)

def load_image(filename, size=None):
    full_path = resource_path(filename)
    image = pygame.image.load(full_path)
    if size:
        image = pygame.transform.scale(image, size)
    return image
