#main way of running the whole program
#maybe use this to import sprite sheets and setup the whole game

import pygame
import constants, levels, player, platforms

def main():
    pygame.init()
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Stick Warfare - Scrolling Action Game")

    player = Player()

    level_list = []
    level_list.append(levels.Level_1(player))

    current_level_no = 0
    current_level = level_list[current_level_no]

    #active_sprite_list = pygame.sprite.Group()
    player_level = current_level

    player.rect.x = 340
    player.rect.y = constant.SCREEN_HEIGHT - player.rect.height
    #active_sprite_list.add(player)

    done = False

    clock = pygame.time.Clock()
