import random
import time

#Parametros
SCREEN_TITLE = "Juego Perdido"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 630
MOVEMENT_SPEED = 6
SPRITE_SCALING = 1
SLEEP = 5
            
def posToCoordX(pos):
    return pos-1
    
def posToCoordY(pos):
    return 10-pos

def set_speed(speed):
    pass

class Piece():
    def __init__(self, char):
        self.X = -1
        self.Y = -1
        self.icon = char

# Clase juego
class LostGame():
    
    def __init__(self):
        self.sprites_list = None
        self.moves = []
        self.doing = 0
        self.started = 0
        self.current_text = "Comienza el juego"
        
    def cargar_matriz(self):
        n=10
        grid = [' '] * n
        for i in range(n):
            grid[i] = [' '] * n
        for p in self.sprites_list:
            if p.X != -1:
                grid[p.X][p.Y] = p.icon
        return grid

    def setup(self):
            self.sprites_list = []
        
    def poner_pieza(self, ascii_char, posX, posY, escala=1):
        if len(ascii_char)!=1 or ascii_char == ' ':
            raise Exception('ascii char value not permitted')
        piece_sprite = Piece(ascii_char)
        piece_sprite.X = posToCoordX(posX)
        piece_sprite.Y = posToCoordY(posY)
        self.sprites_list.append(piece_sprite)

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
        move = [True,"",""]
        self.moves.append(move)


    def imprimir_matriz(self, matriz, msg = ""):
    
        line = msg + "\n"
        row = 10
        for i in range(0,10):
            line += "   -----------------------------------------\n"
            if row >= 10:
                line += str(row)+" |"
            else:
                line += str(row)+"  |"
            row -= 1
            for j in range(0,10):
                line += " {} |".format(matriz[j][i])
                
            line += "\n"
        line += "   -----------------------------------------\n"
        line += "     1   2   3   4   5   6   7   8   9   10\n\n\n"
        
        print(line)
            
    def run(self, delta=1):
        tablero = self.cargar_matriz()
        self.imprimir_matriz(tablero, self.current_text)
        for mov in self.moves:
            if type(mov[0]) == type(""):
                self.current_text = mov[0]
                
            elif type(mov[0]) == type(True):
                tablero = self.cargar_matriz()
                self.imprimir_matriz(tablero, self.current_text)

            else:
                if mov[1] < 0:
                    self.sprites_list[mov[0]].X = -1

                else:
                    self.sprites_list[mov[0]].X = mov[1]
                    self.sprites_list[mov[0]].Y = mov[2]
                
                tablero = self.cargar_matriz()
                self.imprimir_matriz(tablero, self.current_text)