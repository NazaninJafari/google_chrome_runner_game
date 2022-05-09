import arcade
import random

class Caktus(arcade.Sprite):
    def __init__(self, s):
        super().__init__()
        self.pic = random.choice(['hug.png','cac2.png','cac3.png','cac11.png'])
        #,'cactus3.png','cactus11.png'
        self.texture = arcade.load_texture(self.pic)
        self.width = 130
        self.height = 150
        self.center_x = 800
        self.center_y = 100
        self.speed = s
        self.change_x = -1 * self.speed
        self.change_y = 0
        
class Bird(arcade.AnimatedWalkingSprite):
    def __init__(self , y):
        super().__init__() 
        self.walk_left_textures = [arcade.load_texture('bird1.jpeg'), arcade.load_texture('bird2.jpeg')]
        
        self.width = 50
        self.height = 50
        self.center_x = 800
        self.center_y = y
        self.speed = 2
        self.change_x = -3
        self.change_y = 0