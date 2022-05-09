import arcade

class Ground(arcade.Sprite):
    def __init__(self, x):
        super().__init__()
        self.texture = arcade.load_texture('terre2.jpg')
        self.width = 100
        self.height = 100
        self.center_x = x
        self.center_y = 50