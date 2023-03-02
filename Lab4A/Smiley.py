import pygame
from pygame.locals import *
from Smiley import *
from Block import *

class Smiley():

    def __init__(self,x_pos=10, y_pos=10):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.img = pygame.image.load('Smiley.jpg')

    def __str__(self):
        return 'Position=({},{}), Height={}, Width={}, Color={}'.format(
            self.x_pos, self.y_pos, self.height, self.width, self.color)

    def change_x(self,x):
        self.x_pos = self.x_pos + x

    def change_y(self,y):
        self.y_pos = self.y_pos + y

    def change_color(self,c):
        self.color = c

    def draw(self, window):
        window.blit(self.img,(self.x_pos,self.y_pos))

    def move_down(self):
        self.y_pos += 10

    def move_up(self):
        self.y_pos -= 10

    def move_right(self):
        self.x_pos += 10

    def move_left(self):
        self.x_pos -= 10

    def get_rect(self):
        my_rect = self.img.get_rect()
        return (self.x_pos,self.y_pos,my_rect[2],my_rect[3])
    
    def collision(self, other):
        if (self.y_pos + 50 >= other.y_pos and self.y_pos <= other.y_pos + 50) and (self.x_pos + 50 >= other.x_pos and self.x_pos <= other.x_pos + 50):
            return True
        
        
        
        #if self.y_pos < (other.y_pos + 51):
            #if ((self.x_pos > other.x_pos and self.x_pos < (other.x_pos + 51)) or ((self.x_pos + 51) > other.x_pos and (self.x_pos + 51) < (other.x_pos + 51))):
                #return True
            #elif ((self.y_pos > other.y_pos and self.y_pos < (other.y_pos - 51)) or ((self.y_pos - 51) > other.y_pos and (self.y_pos - 51) < (other.y_pos - 51))):
                #return True
        #if (self.x_pos >= other.x_pos and self.x_pos <= (other.x_pos + 50) and (self.y_pos >= other.y_pos and self.y_pos <= (other.y_pos + 50))):
            #return True
        #if (self.x_pos >= other.x_pos and (self.x_pos + 50) <= other.x_pos and (self.y_pos >= other.y_pos and (self.y_pos + 50) <= other.y_pos)):
            #return True
        #else:
            #return False