from os import remove
import arcade
import random
import time

from dinosaur import Dinosaur
from cactusbird import Caktus , Bird
from terre import Ground

class Game(arcade.Window):
    def __init__(self):
        super().__init__(Screen_width ,Screen_height, 'google chrome runner')
        self.morning_bacg = arcade.load_texture('morning.jpg')
        self.night_bacg = arcade.load_texture('night1.jpg')
        self.change_backg = 0
        self.start_time = time.time()
        self.time_chang_bacg = time.time()
        self.bird_time = time.time()
        self.score_time = time.time()
        self.sound = arcade.load_sound(':resources:sounds/jump3.wav')
        self.game_over = False
        self.gravity = 0.2
        self.sp = 4
        self.score = 0
        self.high_score = 0
        self.me = Dinosaur()
        self.bird_list = arcade.SpriteList()
        self.cactus_list = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()
        
        for i in range(0,1000,100):
            ground = Ground(i)
            self.ground_list.append(ground)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.me, self.ground_list, self.gravity)    
    
    def on_draw(self):
        
        if self.game_over == True:
            arcade.draw_text('Game Over', 250, 400, arcade.color.ORANGE ,50)
            arcade.draw_text('press Space for retry', 200, 300, arcade.color.PINK, 40)
        else:    
            arcade.start_render()
            
            if self.change_backg == 1:
                arcade.draw_lrwh_rectangle_textured(0, 0, Screen_width, Screen_height, self.night_bacg)
            else:
                arcade.draw_lrwh_rectangle_textured(0, 0, Screen_width, Screen_height, self.morning_bacg)
      
            for g in self.ground_list:
                g.draw()
            
            self.me.draw()
            
            for cactus in self.cactus_list:
                cactus.draw()
            
            for b in self.bird_list :
                b.draw()
            #show scores
            if self.change_backg == 0 :
                arcade.draw_text('Score: '+ str(self.score) , 600, 550, arcade.color.BLACK, 20 ,font_name='arial')
                arcade.draw_text('High Score: '+ str(self.high_score), 350 ,550, arcade.color.BLACK, font_size= 20, font_name='arial')
            else:
                arcade.draw_text('Score: '+ str(self.score) , 600, 550, arcade.color.WHITE, 20 ,font_name='arial')
                arcade.draw_text('High Score: '+ str(self.high_score), 350 ,550, arcade.color.WHITE, font_size= 20, font_name='arial')
                
    def on_update(self, delta_time: float):
        
        self.physics_engine.update()
        self.me.update_animation()
        
        for cactus in self.cactus_list:
            cactus.update()
            if cactus.center_x < 0:
                self.cactus_list.remove(cactus)
        
        self.end_time = time.time()
        if self.end_time - self.score_time > 0.2 :
            self.score += 1
            self.score_time = time.time()

        self.end_time = time.time()
        if self.end_time - self.start_time > 3 :        
            self.cactus_list.append(Caktus(self.sp))
            self.start_time = time.time()
            self.sp += 0.05
        
        self.end_time = time.time()
        if self.end_time - self.time_chang_bacg > 10:
            if self.change_backg == 0:
                self.change_backg = 1
            else:
                self.change_backg = 0     
            self.time_chang_bacg = time.time()    
        
        if self.score >= 1000:
            self.end_time = time.time() 
            if self.end_time - self.bird_time > 4:
                y = random.randint(240,350)
                bird = Bird(y)
                self.bird_list.append(bird)
                self.bird_time = time.time()
        
        for b in self.bird_list:
            if arcade.check_for_collision(self.me , b):
                self.game_over = True
        
        for cactus in self.cactus_list:
            if arcade.check_for_collision(self.me , cactus):
                self.game_over = True
        
        for b in self.bird_list :
            b.update()
            b.update_animation()
            if b.center_x < 0:
                self.bird_list.remove(b)        

    def on_key_press(self, symbol: int, modifiers: int):
        
        if symbol == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.me.change_y = 12
                arcade.play_sound(self.sound)     

        elif symbol == arcade.key.DOWN:
            self.me.walk_down_textures = [arcade.load_texture('downdino1.png'), arcade.load_texture('downdino.png'), arcade.load_texture('left.png'),arcade.load_texture('right.png')]           
        
        elif symbol == arcade.key.SPACE:
            #start new game:
            self.game_over = False
            if self.score > self.high_score :
                self.high_score = self.score
            self.score = 0
            self.sp = 4
            self.start_time = time.time()
            self.time_chang_bacg = time.time()
            self.bird_time = time.time()
            self.score_time = time.time()
    
    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_y = 0
        #if symbol == arcade.key.DOWN:
        self.me.walk_down_textures = [arcade.load_texture('right.png'), arcade.load_texture('left.png')]
                  

Screen_width = 800
Screen_height = 600

game = Game()
arcade.run()