# Import pygame library
import pygame
pygame.init() 
# Create a game screen and set its title
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Breakout Game")
# Define the RGB color combinations of rectangle objects
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,150,0)
YELLOW = (255,255,0)
# Create a paddle and a ball rectangle objects
paddle = pygame.Rect(300,500,60,10)
ball = pygame.Rect(200,250,10,10)
# Define variables to track ball and paddle movement
ballx = -1
bally = -1
paddlex = 2
# Create a variable to store player score and name it as "score"
score = 0

# Create a variable to store player lives and name it as "lives". Set its value as 3.
lives = 5

# Create red, orange and yellow bricks
bricksR = [pygame.Rect(10+i*100, 60, 80, 30) for i in range(6)]  
bricksO = [pygame.Rect(10+i*100, 100, 80, 30) for i in range(6)]    
bricksY = [pygame.Rect(10+i*100, 140, 80, 30) for i in range(6)]

# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                  carryOn = False  
    screen.fill(DARKBLUE)
    # Check for user input to move the paddle
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if paddle.x<540: 
                paddle.x+=paddlex
        if event.key == pygame.K_LEFT:
            if paddle.x>0:
                paddle.x-=paddlex
           
    pygame.draw.line(screen, WHITE, [0, 38], [600, 38], 2)
    pygame.draw.rect(screen,LIGHTBLUE,paddle)
    font = pygame.font.Font(None, 34)
    # Insert code to display score text here after converting "score" to sting datatype
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    
    # Insert code to display lives text here after converting "lives" to sting datatype
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (500,10))
    
    # Update x and y position of the ball on screen 
    ball.x = ball.x + ballx
    ball.y = ball.y + bally
    # Limiting ball movement on screen along x-axis
    if ball.x >= 590:
      ballx = -ballx
    if ball.x <= 10:
      ballx = -ballx
    # Limiting ball movement on screen along y-axis
    if ball.y >= 590:
      bally = -bally
    if ball.y <= 10:
      bally = -bally
    pygame.draw.rect(screen,WHITE ,ball)
    # Check for paddle and ball collision and change the ball direction if they collided
    if paddle.collidepoint(ball.x, ball.y):
        bally = -bally
    
    # Draw the red bricks on game screen here
    for i in bricksR:
        pygame.draw.rect(screen,RED,i)
    # Draw the orange bricks on game screen here
    for i in bricksO:
        pygame.draw.rect(screen,ORANGE,i)
    # Draw the yellow bricks on game screen here
    for i in bricksY:
        pygame.draw.rect(screen,YELLOW,i)
    
    # Code for red brick and ball collision here
    for i in bricksR:
        if i.collidepoint(ball.x,ball.y):
            bricksR.remove(i)
            ballx = -ballx
            bally = -bally
            score += 3
    # Code for orange brick and ball collision here
    for i in bricksO:
        if i.collidepoint(ball.x,ball.y):
            bricksO.remove(i)
            ballx = -ballx
            bally = -bally
            score += 3
    # Code for yellow brick and ball collision here
    for i in bricksY:
        if i.collidepoint(ball.x,ball.y):
            bricksY.remove(i)
            ballx = -ballx
            bally = -bally
            score += 3
            
    # Code for loss of life and displying number of lives left 
    if ball.y >= 510:
        # Decrease "lives" by 1   
        lives -= 1
        # Display "LOST A LIFE" text
        font = pygame.font.Font(None, 74)
        text = font.render("LOST A LIFE", 1, WHITE)
        screen.blit(text, (150,250))
        # Display "Lives left"
        font = pygame.font.Font(None, 34)
        text = font.render("Lives left: " + str(lives), 1, WHITE)
        screen.blit(text, (150,300))
        pygame.display.flip()
        # Reset ball position
        ball.x = 200
        ball.y = 250
        # Allow user some time to adjust before playing the next round
        pygame.time.wait(1000)
        
    # Code for breaking game loop
    if lives == 0:
        # Display Game Over
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, RED)
        screen.blit(text, (150,330))
        pygame.display.flip()
        # Add some delay before closing the game window
        pygame.time.wait(2000)
        # Break the loop using the keyword 'break' 
        break
    
    # Stop the game when the user wins a maximum score of 54 
    if score == 54:
        # Use the same styling as "GAME OVER" but display "YOU WON" in yellow color
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON!!", 1, YELLOW)
        screen.blit(text, (150,350))
        pygame.display.flip()
        # Add some delay before closing the game window
        pygame.time.wait(2000)
        # Break the loop using the keyword 'break'
        break
   
    pygame.time.wait(5)
    # Update the contents of entire display
    pygame.display.flip()
# Quit the game  
pygame.quit()