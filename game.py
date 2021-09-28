# Import pygame to allow for specified functions created for games. 
# Import random to allow a random entry point of an image.

import pygame
import random

# Initialize the pygame modules to get everything started.

pygame.init() 

# Create and set the screen with specified width and height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

# Use pygame image load to create the images of the player, 3 monsters and a prize. 
# Pygame convert will also allow for image re-sizing.

player = pygame.image.load("player.jpg").convert()
monster = pygame.image.load("monster.jpg").convert()
monster1 = pygame.image.load("monster.jpg").convert()
monster2 = pygame.image.load("monster.jpg").convert()
prize = pygame.image.load("prize.jpg").convert()

# Create new width and height for re-sizing the images.
# The image's width and height will also allow for detection of boundries.

player_height = 80
player_width = 80
monster_height = 50
monster_width = 50
monster1_height = 50
monster1_width = 50
monster2_height = 50
monster2_width = 50
prize_height = 80
prize_width = 80

# Use pygame transform scale to form new image sizes.

player = pygame.transform.scale(player, (80, 80))
monster = pygame.transform.scale(monster, (50, 50))
monster1 = pygame.transform.scale(monster1, (50, 50))
monster2 = pygame.transform.scale(monster2, (50, 50))
prize = pygame.transform.scale(prize, (80, 80))

# Store the positions(coordinates x, width and y, height) of all your images as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

prizeXPosition = 880
prizeYPosition = 440

# Make the monsters start off screen positions:
# Monster enters from the right, monster1 enters from the left and monster2 from the top.

monsterXPosition =  screen_width
monsterYPosition =  random.randint(0, screen_height - monster_height)

monster1XPosition = (0)
monster1YPosition = random.randint(0, screen_height - monster1_height)

monster2XPosition = random.randint(0, screen_width - monster2_width)
monster2YPosition = (0)

# Create a boolean value of False to check if the up or down key is pressed.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# Use a nested while loop to create real time game play.
# Use pygame blit to clear screen and draw the images to their coordinates on the screen.
# Use pygame update to update the screen and loop through the events.

while 1: 

    screen.fill(0)
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(monster, (monsterXPosition, monsterYPosition))
    screen.blit(monster1, (monster1XPosition, monster1YPosition))
    screen.blit(monster2, (monster2XPosition, monster2YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip() 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        
        # This event checks if the user presses a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # The coordinate system of pygame is top left corner is (x, 0 and y, 0).
    # Set the movement of the player to increment as the up, down, left and right keys are hit.
    # Using coordinates > 0 to screen width or height, prevent player from exiting the screen.
      
    if keyDown == False:
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyUp == False:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1

    if keyRight == False:
        if playerXPosition > 0:
            playerXPosition -= 1

    if keyLeft == False:
        if playerXPosition < screen_width - player_width:
            playerXPosition += 1
    
    # Check for collision of the monster with the player or player with the prize.
    # Use pygame rect to position rect around images.
    # Update positions to detect collision of images.

    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    monsterBox = pygame.Rect(monster.get_rect())
    monsterBox.top = monsterYPosition
    monsterBox.left = monsterXPosition

    monster1Box = pygame.Rect(monster1.get_rect())
    monster1Box.top = monster1YPosition
    monster1Box.left = monster1XPosition

    monster2Box = pygame.Rect(monster2.get_rect())
    monster2Box.top = monster2YPosition
    monster2Box.left = monster2XPosition

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the player with monsters:
    
    if playerBox.colliderect(monsterBox) or playerBox.colliderect(monster1Box) or playerBox.colliderect(monster2Box):
    
        # Display losing status to the user: 
        
        print("You lose!")
        
        # Quit game and exit window:

        pygame.quit()
        exit(0)

    # Test collision of the player with the prize:

    if playerBox.colliderect(prizeBox):

        # Display winning status to the user:

        print ("You Win!")
       
        # Quit game and exit window:
        
        pygame.quit()
        exit(0)
        
    # If the monsters are off the screen the user wins the game.
    # Set coordinates of monsters to detect screen boundries depending on their entry and exit point.
    
    if monsterXPosition < 0 - monster_width and monster1XPosition > 1040 - monster1_width and monster2YPosition > 680 - monster2_height:
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 

        pygame.quit()
        
        exit(0)
    
 
    
    # Make the monsters approach the player according to their entry points on the screen.
    
    monsterXPosition -= 0.15
    monster1XPosition += 0.15
    monster2YPosition += 0.15
    
    # ================The game loop logic ends here. =============
  
