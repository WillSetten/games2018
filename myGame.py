import time, sys
import pygame
import constants
import levels
from enemy import Enemy
import random
from player import Player
from powerup import PowerUp
def main():
    """ Main Program """
    pygame.init()

    multiplayer = False

    # Set the height and width of the screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    pygame.display.set_caption("Artnoc")
    #add in a scoreboard
    font = pygame.font.Font(None, 28)

    #player1 = Player()
    #player2 = Player()
    #enemy_list = []
    #level_list = []
    #level_list.append(levels.Level_01(player1, player2))
    #current_level = level_list[0]
    #active_sprite_list = pygame.sprite.Group()
    #enemy_sprite_list = pygame.sprite.Group()
    #done = False
    #clock = pygame.time.Clock()
    play = False


    #----------MAIN MENU-----------------


    while True:
        multiplayer = mainMenu(screen, play, multiplayer)
        # Create the player1
        player1 = Player()
        player2 = Player()
        enemy_list = []
        powerup_list = []
        # Create all the levels
        level_list = []
        level_list.append(levels.Level_01(player1, player2))

        # Set the current level
        current_level = level_list[0]

        for i in range(0,3):
            enemy_list.append(Enemy(random.randint(0,1)))
            enemy_list[i].level = current_level
        for i in range(0,4):
            powerup_type = random.randint(2,4)
            powerup_list.append(PowerUp(powerup_type))
            powerup_list[i].level = current_level

        active_sprite_list = pygame.sprite.Group()
        enemy_sprite_list = pygame.sprite.Group()
        powerup_sprite_list = pygame.sprite.Group()
        player1.level = current_level
        if multiplayer==True:
            player2.level = current_level

        for i in range(0,3):
            x = random.randint(constants.SCREEN_WIDTH,constants.SCREEN_WIDTH+1)
            #y = random.randint(0,constants.SCREEN_HEIGHT-5)
            enemy_list[i].spawn(x,0)
            enemy_sprite_list.add(enemy_list[i])
        for i in range(0,1):
            x = random.randint(0,10000)
            powerup_list[i].spawn(x,0)
            powerup_sprite_list.add(powerup_list[i])
        player1.rect.x = 340
        player1.rect.y = constants.SCREEN_HEIGHT - player1.rect.height
        active_sprite_list.add(player1)
        if multiplayer==True:
            player2.rect.x = 340
            player2.rect.y = constants.SCREEN_HEIGHT - player2.rect.height
            active_sprite_list.add(player2)

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        play = True
        newpoweruplength=constants.SCREEN_WIDTH
        powerupflag = False
        #----------END MAIN MENU, START INITIALISATION-------------
        #init(multiplayer)

        # -------- Main Game Loop -----------
        while (player1.lives>0 and player2.lives>0) and (play==True):
            for event in pygame.event.get(): # User did something
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        play = False
                    if event.key == pygame.K_DOWN:
                        player1.prone()
                    if event.key == pygame.K_LEFT:
                        player1.go_left()
                    if event.key == pygame.K_RIGHT:
                        player1.go_right()
                    if event.key == pygame.K_UP:
                        player1.aimup()
                    if event.key == pygame.K_j:
                        player1.jump()
                    if event.key == pygame.K_k:
                        player1.shoot()




                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT and player1.change_x > 0:
                        player1.stop()
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player1.resetaim()
                    if event.key == pygame.K_LEFT and player1.change_x < 0:
                        player1.stop()
                    if event.key == pygame.K_k:
                        player1.stopshooting()#

                if multiplayer==True:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            player2.prone()
                        if event.key == pygame.K_a:
                            player2.go_left()
                        if event.key == pygame.K_d:
                            player2.go_right()
                        if event.key == pygame.K_w:
                            player2.aimup()
                        if event.key == pygame.K_1:
                            player2.jump()
                        if event.key == pygame.K_2:
                            player2.shoot()


                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_d and player2.change_x > 0:
                            player2.stop()
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            player2.resetaim()
                        if event.key == pygame.K_a and player2.change_x < 0:
                            player2.stop()
                        if event.key == pygame.K_2:
                            player2.stopshooting()


            # Update the player1.

            active_sprite_list.update(enemy_list)
            enemy_sprite_list.update(player1)
            powerup_sprite_list.update(player1)
            if multiplayer==True:
                enemy_sprite_list.update(player2)
                powerup_sprite_list.update(player2)

            #update the enemies
            #for enemy in levels.Level.enemy_list:
            #    enemy.update()

            # Update items in the level
            current_level.update()

            # If the player1 gets near the right side, shift the world left (-x)
            if player1.rect.x >= 500:
                diff = player1.rect.x - 500
                player1.rect.x = 500
                current_level.shift_world(-diff)
                current_level.draw(screen)

            # If the player1 gets near the left side, shift the world right (+x)
            if player1.rect.x <= 120:
                diff = 120 - player1.rect.x
                player1.rect.x = 120
                current_level.shift_world(diff)
                current_level.draw(screen)

            if multiplayer==True:
                if player2.rect.x >= 500:
                    diff = player2.rect.x - 500
                    player2.rect.x = 500
                    current_level.shift_world(-diff)
                    current_level.draw(screen)

                if player2.rect.x <= 120:
                    diff = 120 - player2.rect.x
                    player2.rect.x = 120
                    current_level.shift_world(diff)
                    current_level.draw(screen)

            # If the player1 gets to the end of the level, go to the next level
            current_position = player1.rect.x + current_level.world_shift
            if current_position < current_level.level_limit:
                player1.rect.x = 120
                if current_level_no < len(level_list)-1:
                    current_level_no += 1
                    current_level = level_list[current_level_no]
                    player1.level = current_level

            if multiplayer==True:
                current_position = player2.rect.x + current_level.world_shift
                if current_position < current_level.level_limit:
                    player2.rect.x = 120
                    if current_level_no < len(level_list)-1:
                        current_level_no += 1
                        current_level = level_list[current_level_no]
                        player2.level = current_level

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            current_level.draw(screen)
            active_sprite_list.draw(screen)
            enemy_sprite_list.draw(screen)
            powerup_sprite_list.draw(screen)
            for x in enemy_sprite_list:
                    if x.bullet_list!=None:
                        x.bullet_list.draw(screen)
            if multiplayer==True:
                if player1.dead==False and player2.dead==False:
                    if player1.bullet_list!=None:
                        player1.bullet_list.draw(screen)
                    if player2.bullet_list!=None:
                        player2.bullet_list.draw(screen)
            else:
                if player1.dead==False:
                    if player1.bullet_list!=None:
                        player1.bullet_list.draw(screen)
            text = font.render("P1 Score = "+str(player1.score),1,(constants.WHITE))
            screen.blit(text,(0,0))
            if multiplayer==True:
                text = font.render("P2 Score = "+str(player2.score),1,(constants.WHITE))
                screen.blit(text,(0,40))
            text = font.render("Quit to Main Menu (Esc)",1,constants.WHITE)
            screen.blit(text,(constants.SCREEN_WIDTH/2-120,0))
            text = font.render("P1 Lives = "+str(player1.lives),1,(constants.WHITE))
            screen.blit(text,(constants.SCREEN_WIDTH-115,0))
            if multiplayer==True:
                text = font.render("P2 Lives = "+str(player2.lives),1,(constants.WHITE))
                screen.blit(text,(constants.SCREEN_WIDTH-115,40))
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

            # Limit to 60 frames per second
            clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

def mainMenu(screen, play, multiplayer):
    play = False
    screen.fill(constants.BLACK)
    title = pygame.font.Font(None,180)
    textsurf = title.render("ARTNOC", True, constants.WHITE)
    textrect = (constants.SCREEN_WIDTH/2-530,constants.SCREEN_HEIGHT/2-250)
    screen.blit(textsurf, textrect)
    pygame.display.update()
    title = pygame.font.Font(None,75)
    font = pygame.font.Font(None, 45)
    text1 = title.render("Single Player", True, constants.WHITE)
    screen.blit(text1, (constants.SCREEN_WIDTH/2-530, constants.SCREEN_HEIGHT/2-100))
    text1 = title.render("Multi Player", True, constants.WHITE)
    screen.blit(text1, (constants.SCREEN_WIDTH/2-530, constants.SCREEN_HEIGHT/2+50))
    text1 = title.render("Quit", True, constants.WHITE)
    screen.blit(text1, (constants.SCREEN_WIDTH/2-530, constants.SCREEN_HEIGHT/2+200))
    title = pygame.font.Font(None, 70)
    text1 = title.render("Player 1 controls:", True, constants.RED)
    screen.blit(text1, (constants.SCREEN_WIDTH/2+100, constants.SCREEN_HEIGHT/2-100))
    text2 = font.render("Move = Arrow Keys", True, constants.RED)
    text3 =font.render("Jump = J    Shoot = K", True, constants.RED)
    screen.blit(text2, (constants.SCREEN_WIDTH/2+100, constants.SCREEN_HEIGHT/2-20))
    screen.blit(text3, (constants.SCREEN_WIDTH/2+100, constants.SCREEN_HEIGHT/2+50))
    text1 = title.render("Player 2 controls:", True, constants.RED)
    screen.blit(text1, (constants.SCREEN_WIDTH/2+100, constants.SCREEN_HEIGHT/2+130))
    text2 = font.render("Move = W A S D", True, constants.RED)
    text3 =font.render("Jump = 1    Shoot = 2", True, constants.RED)
    screen.blit(text2, (constants.SCREEN_WIDTH/2+100, constants.SCREEN_HEIGHT/2+210))
    screen.blit(text3, (constants.SCREEN_WIDTH/2+100, constants.SCREEN_HEIGHT/2+280))
    arrow = title.render(">", True, constants.WHITE)

    apos1 = (constants.SCREEN_WIDTH/2-570, constants.SCREEN_HEIGHT/2-100)
    apos2 = (constants.SCREEN_WIDTH/2-570, constants.SCREEN_HEIGHT/2+50)
    apos3 = (constants.SCREEN_WIDTH/2-570, constants.SCREEN_HEIGHT/2+200)
    poslist = [apos1,apos2,apos3]
    point = 0

    pygame.display.update()
    while play == False:
        pygame.draw.rect(screen,constants.BLACK,(constants.SCREEN_WIDTH/2-570,constants.SCREEN_HEIGHT/2-100,27,350))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if point>1:
                        point = 0
                    else:
                        point += 1
                if event.key == pygame.K_UP:
                    if point<1:
                        point = 2
                    else:
                        point-=1
                if event.key == pygame.K_RETURN:
                    if point == 1:
                        multiplayer = True
                        play = True
                    elif point == 0:
                        multiplayer = False
                        play = True
                    else:
                        sys.exit()
        screen.blit(arrow, poslist[point])
        pygame.display.flip()
    screen.fill((0,0,0))
    pygame.display.flip()
    return multiplayer


if __name__ == "__main__":
    main()
