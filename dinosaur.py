import arcade

class Dinosaur(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 150
        self.center_x = 150
        self.center_y = 200
        
        self.stand_right_textures = [arcade.load_texture('standdino1.png')] 
        self.walk_right_textures = [arcade.load_texture('right.png'), arcade.load_texture('left.png')]
        self.walk_left_textures = [arcade.load_texture('right.png'), arcade.load_texture('left.png')]        
        self.walk_down_textures = [arcade.load_texture('left.png')]
        self.walk_up_textures = [arcade.load_texture('standdino1.png')]
        #self.stand_right_textures = [arcade.load_texture('standdino1.png'), arcade.load_texture('right.png'), arcade.load_texture('left.png')]