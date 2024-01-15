#Michael Han, 101157504, Tutorial 10
#pygame template
import pygame
import random
import math
#some system parameters
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
NUMBER_OF_BALLS=1

class Ball:
    def __init__(self,x,y,deg,color,size):
        self.x=x
        self.y=y
        self.deg=random.randint(0,360)
        self.color=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        self.size=20

    def move(self):
        
        self.x+=math.cos(math.radians(self.deg))
        self.y+=math.sin(math.radians(self.deg))
        #if self.x+self.size goes beyond right screen
        if self.x+self.size>=WINDOW_WIDTH:  
            #change direction
            self.deg=180-self.deg
            #change color
            self.changeColor(255,0,0)
        #left wall
        if self.x+self.size <= 0:
            self.deg=180-self.deg
            self.changeColor(0,0,255)

        #if self.y+self.size goes beyond the bottom of screen
        if self.y+self.size>=WINDOW_HEIGHT:
            #change direction
            self.deg=360-self.deg
            #change color
            self.changeColor(128,0,128)
        #top wall
        if self.y +self.size <= 0:
            #change direction
            self.deg=360-self.deg
            #change color
            self.changeColor(0,255,0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [int(self.x),int(self.y)],self.size)
    def changeColor(self, num1, num2, num3):
        self.color=[num1,num2,num3]

def main():

    screen = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])
    clock = pygame.time.Clock()
	
	#initialize the system
    balls=[]
    for i in range(NUMBER_OF_BALLS):
        balls.append(Ball(400,400,random.randint(0,360),[random.randint(0,255),random.randint(0,255),random.randint(0,255)],20))
    
    #simulation loop:
    running = True
    while running:
		
        events = pygame.event.get()
        for event in events:
            #handle exit events
            if event.type==pygame.QUIT:
                running = False
            #handle user input
            if event.type==pygame.MOUSEBUTTONDOWN:
                #adding new ball at mouse position
                balls.append(Ball(event.pos[0],event.pos[1],random.randint(0,360),[random.randint(0,255),random.randint(0,255),random.randint(0,255)],20))
           

		#draw background
        screen.fill([255,255,255])
		
		#draw foreground
        for i in range(len(balls)):
            balls[i].draw(screen)
		
		#move objects
        for i in range(len(balls)):
            balls[i].move()
        
            
        #refresh
        pygame.display.flip()
        clock.tick(300)  

main()