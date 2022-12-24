import pygame, sys


pygame.init()
clock = pygame.time.Clock()

#main window
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Omega Balls')

#making ball
ball_width = 30
ball_height = 30
ball = pygame.Rect(screen_width/2-ball_width/2, screen_height/2-ball_height/2, ball_width, ball_height)

#ground
groundWidth = 1200
groundHeight = 25
ground = pygame.Rect(0, screen_height - groundHeight, groundWidth, groundHeight)

#goal
goal_width = 10
goal_height = 110
goal1 = pygame.Rect(screen_width-20, screen_height- groundHeight -110, goal_width, goal_height)
goal2 = pygame.Rect(10, screen_height- groundHeight -110, goal_width, goal_height)

bgColor = pygame.Color("grey12")
white = (255,255,255)
green = pygame.Color("green")

#ball
ballSpeedX = 0
ballSpeedY = 0
deceleration = 0.97
acceleration = 0.8

def ballHandling():
    global ballSpeedX
    global ballSpeedY
    global deceleration
    global acceleration

    if ball.top < 0: 
        ballSpeedY *= -1
    if ball.bottom > screen_height - groundHeight:
        ballSpeedY *= -1
        deceleration *= 0.99

    if ball.left <= 0 or ball.right > screen_width:
        ballSpeedX *= -1
    #move ball
    ball.x += ballSpeedX
    ball.y += ballSpeedY 
    ballSpeedX *= deceleration
    if ballSpeedY < 0:
        ballSpeedY *= deceleration

    # gravity
    ballSpeedY += acceleration
    
# ball stop control
    if ballSpeedX <= 0.3 and ballSpeedX >= -0.3:
        ballSpeedX = 0
    if ballSpeedY <= 0.3 and ballSpeedY >= -0.3:
        ballSpeedY = 0
    if deceleration <= 0.85:
        deceleration = 0
        acceleration = 0
        ballSpeedY = 0

def drawObjects():
#visuals
    screen.fill(bgColor)
    pygame.draw.rect(screen, white, goal1)
    pygame.draw.rect(screen, white, goal2)    
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (screen_width/2,0), (screen_width/2, screen_height))

    pygame.draw.rect(screen, green, ground)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #ball handling
    ballHandling()
    drawObjects()

    pygame.display.flip()
    clock.tick(60)