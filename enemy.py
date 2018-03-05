import pygame, time
#constructor should work by being called with an enemy type, then will set it up accordingly
#assuming the main game class will select an enemy type and when to spawn it?
#can discuss these issues in the week somewhen
#Also not sure on how to track shots fired, whether to work them out in attacker class
#or in the person who fired the shot
class Enemy:
    def __init__(self, type):/
        if (type=="Infantry"):
            self.health = 1
            self.speed = 10 #value to be discussed later on
            self.type = type
            self.pos = Vector(0,0)
            self.sprite = null #set as null for now while working on other areas
        elif (type=="Heavy"):
            self.health = 3
            self.speed = 0
            self.type = type
            self.pos = Vector(0,0)
            self.sprite = null
#        elif (type=="Drone"):
#            self.health = 3
#            self.speed = 5
#            self.type = type
#            self.pos = Vector(0,0)
#            self.sprite = null
        else:
            self.health = 40
            self.speed = 0
            self.type = type
            self.pos = Vector(0,0)
            self.sprite = null

    def play(self):
        spawn()
        while (self.health>0):
                if (self.type=="Infantry"):
                    move()
                    checkIfHit()
                else:
                    attack()
                    checkIfHit()
                    #runs as per usual
                    #if player shot hits enemy
                        #hit()

    def spawn(self):
        #finds an empty platform - need implementation from platform class
        #set self.pos to a place on platform off screen (account for sprite size etc)

    def attack(self):
            #work out vector from enemy to player
            #fire shot, work out sprite/object to be fired
            #need to consider power ups etc.

    def move(self):
        self.pos.x=self.pos.x+1
        #only triggered if the enemy type is infantry
        #if distance between enemy and player is less than x
        #attack user - infantry attack needs to be run

    def checkIfHit(self):
    #


    #triggered if the user has been hit
        self.health=self.health-1
        if (self.health<1):
            remove()
            #if the enemy is dead, remove it from the game
            if (self.type=="Boss"):
                #score = score + 5000
            elif (self.type=="Heavy"):
                #score = score + 500
            elif (self.type=="Drone"):
                #score = score + 250
            else:
                #score = score + 100
            #increment score since the user has killed an enemy
        #potentially display different sprite if hit / blur sprite for x amount of time to indicate hit

    def remove(self):
        self.sprite = null #set to a blank sprite so it no longer appears
        #will run if the enemy is dead, to remove them from the environment
