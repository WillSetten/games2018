#main way of running the whole program
#maybe use this to import sprite sheets and setup the whole game

import pygame
import constants
import levels
import player

def main():
    pygame.init()
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Stick Warfare - Scrolling Action Game")
    #initalises Player
    player = Player()
    #creates all levels
    level_list = []
    level_list.append(levels.Level_1(player))
    #sets current Level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player_level = current_level

    player.rect.x = 340
    player.rect.y = constant.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
    #loop until user quits the game
    done = False
    #manages how fast screen updates
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get(): #if user does something
            if event.type == pygame.QUIT: #game closed
                done = True
            if event.type == pygame.KEYDOWN: #key pressed
                if event.key == pygame.K_LEFT:
                    player.moveLeft()
                if event.key == pygame.K_RIGHT:
                    player.moveRight()
                if event_key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP: #key released
                if event.key == pygame.K_LEFT and player.changeX < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.changeX > 0:
                    player.stop()

            #update player
            active_sprite_list.update()

            #update items in level
            current_level.update()

            # If the player gets near the right side, shift the world left (-x)
            if player.rect.right >= 500:
                diff = player.rect.right - 500
                player.rect.right = 500
                current_level.shift_world(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if player.rect.left <= 120:
                diff = 120 - player.rect.left
                player.rect.left = 120
                current_level.shift_world(diff)

            current_level.draw(screen)
            active_sprite_list.draw(screen)

            #60fps
            clock.tick(60)

            #update SCREEN
            pygame.display.flip()
        pygame.quit()

    if __name__ == "__main__":
        main()
