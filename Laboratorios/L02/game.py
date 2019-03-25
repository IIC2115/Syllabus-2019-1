import random
import arcade
import time

#Parametros
SCREEN_TITLE = "Juego Perdido"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 630
MOVEMENT_SPEED = 6
SPRITE_SCALING = 1
SLEEP = 5
            
def posToCoordX(pos):
    return 60*(pos-1)+30
    
def posToCoordY(pos):
    return 60*(pos-1)+60

def set_speed(speed):
    global MOVEMENT_SPEED, SLEEP
    if speed == 1:
        MOVEMENT_SPEED = 1
        SLEEP = 5
    elif speed == 2:
        MOVEMENT_SPEED = 6
        SLEEP = 5
    elif speed == 3:
        MOVEMENT_SPEED = 10
        SLEEP = 2
    else:
        MOVEMENT_SPEED = 60
        SLEEP = 0


# Clase juego
class LostGame(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.sprites_list = None
        self.background = None
        arcade.set_background_color(arcade.color.RED)
        self.moves = []
        self.doing = 0
        self.started = 0
        self.current_text = "Comienza el juego"

    def setup(self):
        self.background = arcade.load_texture("sprites/chess_background.png")
        self.sprites_list = arcade.SpriteList()
        
    def poner_pieza(self, nombreArchivo, posX, posY, escala):
        piece_sprite = arcade.Sprite("sprites/" + nombreArchivo, escala)
        piece_sprite.center_x = posToCoordX(posX)
        piece_sprite.center_y = posToCoordY(posY)
        self.sprites_list.append(piece_sprite)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2)+15, SCREEN_WIDTH, SCREEN_HEIGHT-30, self.background)
        self.sprites_list.draw()
        output = f"{self.current_text}"
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 14)

    def mover_pieza(self, nPieza, posX, posY):
        move = [nPieza,posToCoordX(posX),posToCoordY(posY)]
        self.moves.append(move)
        
    def quitar_pieza(self, nPieza):
        move = [nPieza,-1,-1]
        self.moves.append(move)
        
    def mostrar_texto(self, texto):
        move = [texto,"",""]
        self.moves.append(move)
    
    def fin_del_juego(self):
        move = [False,False,False]
        self.moves.append(move)
            
    def update(self, delta_time):
        
        # Espera de 1 segundo antes de comenzar
        if self.started < 2:
            time.sleep(SLEEP/10)
            self.started += 1
            
        # Solo se ejecuta si ya comenzamos y quedan doings
        if (len(self.moves) >= self.doing + 1) and (self.started == 2):
            if type(self.moves[self.doing][0]) == type(""):
                self.current_text = self.moves[self.doing][0]
                time.sleep(SLEEP/20)
                self.doing+=1
                
            elif type(self.moves[self.doing][0]) == type(False):
                time.sleep(SLEEP)
                arcade.close_window()

                
            else:
                if self.moves[self.doing][1] < 0:
                    self.sprites_list[self.moves[self.doing][0]].center_x += 1000
                    time.sleep(SLEEP/10)
                    self.doing +=1
                    return
                
                if self.sprites_list[self.moves[self.doing][0]].center_x < self.moves[self.doing][1]:
                    self.sprites_list[self.moves[self.doing][0]].center_x += MOVEMENT_SPEED
                    self.sprites_list[self.moves[self.doing][0]].change_x = 0
                    self.sprites_list[self.moves[self.doing][0]].change_y = 0
               
                elif self.sprites_list[self.moves[self.doing][0]].center_x > self.moves[self.doing][1]:
                    self.sprites_list[self.moves[self.doing][0]].center_x += -MOVEMENT_SPEED
                    self.sprites_list[self.moves[self.doing][0]].change_x = 0
                    self.sprites_list[self.moves[self.doing][0]].change_y = 0
        
                elif self.sprites_list[self.moves[self.doing][0]].center_y < self.moves[self.doing][2]:
                    self.sprites_list[self.moves[self.doing][0]].center_y += MOVEMENT_SPEED
                    self.sprites_list[self.moves[self.doing][0]].change_x = 0
                    self.sprites_list[self.moves[self.doing][0]].change_y = 0
         
                elif  self.sprites_list[self.moves[self.doing][0]].center_y > self.moves[self.doing][2]:
                    self.sprites_list[self.moves[self.doing][0]].center_y += -MOVEMENT_SPEED
                    self.sprites_list[self.moves[self.doing][0]].change_x = 0
                    self.sprites_list[self.moves[self.doing][0]].change_y = 0
                else:
                    self.doing+=1
                    time.sleep(SLEEP/20)