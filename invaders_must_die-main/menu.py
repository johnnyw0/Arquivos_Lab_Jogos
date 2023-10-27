from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.collision import *
import random

#constantes
HEIGHT = 772
WIDTH = 564
#subclasses de sprite pra encapsular o código e tornar os loops mais legiveis
class Shot(Sprite):
    img = {"player":"assets/shot.png", "enemy":"assets/shot_enemy.png"}
    vel = HEIGHT/2
    def __init__(self, x, y, tipo='player'):
        super().__init__(Shot.img[tipo])
        self.set_position(x, y-self.height)
        #self.set_sequence_time(0, 3, 500, loop=True)
        #self.play()
        self.direction = -1 if tipo == "player" else 1

    def move(self, delta_time):
        self.move_y(Shot.vel*delta_time*self.direction)

class Explosion(Sprite):
    img = 'assets/explosion.png'
    def __init__(self, x, y):
        super().__init__(Explosion.img, 4)
        self.set_position(x, y)
        self.set_sequence_time(0, 3, 500, loop=False)
        self.play()

class Enemy(Sprite):
    img = 'assets/enemy.png'
    def __init__(self, x, y):
        super().__init__(Enemy.img, 3)
        self.set_position(x, y)
        self.set_sequence_time(0, 2, 1000)
        self.play()

class Player(Sprite):
    img = 'assets/navi_smol.png'
    def __init__(self):
        super().__init__(Player.img)
        self.set_position(WIDTH/2, HEIGHT- self.height- 20)
        self.hp = [Sprite('assets/hitpoint_.png', 4) for i in range(3)]
        for hitpoint in self.hp:
            hitpoint.set_sequence_time(0, 3, 250)
            hitpoint.play()

    def _draw_(self):
        self.draw()
        for i,hitpoint in enumerate(self.hp):
            hitpoint.set_position(10 +30*i, 20)
            hitpoint.update()
            hitpoint.draw()

    def hit(self):
        self.hp.pop()
        if len(self.hp) == 0:
            #game over
            self.hide()

    def add_hp(self):
        self.hp.append(Sprite('assets/hitpoint_.png', 4))
        self.hp[-1].set_sequence_time(0,3,250)
        self.hp[-1].play()

#matriz de inimigos
#inicia EnemyMatrix(n_de_linhas)
#controla os Enemy objects
class EnemyMatrix(list):
    vel = WIDTH/5
    def __init__(self, rows):
        self.rows = rows
        self.cols = 5
        self.explosions = []
        for i in range(rows):
            self.append([Enemy(75*n, 50+ 75*i) for n in range(self.cols)])
    
    @property
    def alive(self):
        #checa se a matriz ainda tem inimigos vivos
        for row in self:
            for e in row:
                if e.drawable:
                    return True
        return False

    def shoot(self, shot_list):
        i = 0
        if not self.alive:
            return
        while i < dificuldade+1:
            choosen = self[random.randint(0, self.rows-1)][random.randint(0, self.cols-1)]
            if choosen.drawable:
                shot_list.append(Shot(choosen.x+choosen.width/2, choosen.y+choosen.height, tipo='enemy'))
            else:
                continue
            i += 1

    def draw(self):
        for row in self:
            for enemy in row:
                enemy.update()
                enemy.draw()
        for ex in self.explosions:
            if not ex.is_playing():
                self.explosions.remove(ex)
            else:
                ex.update()
                ex.draw()

    def move(self, dt, direction):
        if direction:
            for row in self:
                for enemy in row:
                    enemy.move_x(EnemyMatrix.vel*dt*direction)
                    if enemy.x < 0 or enemy.x + enemy.width > WIDTH:
                        enemy.x = 0 if enemy.x < 0 else WIDTH - enemy.width

    def collision(self, shot):
        global score, dificuldade
        for row in self:
            for e in row:
                if not e.drawable:
                    continue
                #collided_perfect não dá conta do recado sozinho
                if shot.x+shot.width/2 > e.x and shot.x+shot.width/2 < e.x+e.width:
                    if Collision.collided_perfect(e, shot):
                        score += 10*dificuldade
                        shot.hide()
                        e.hide()
                        self.explosions.append(Explosion(e.x+e.width/2, e.y+e.height/2))
                        break
            
#retorna se determinado botão da interface grafica do jogo foi pressionado, recebe o botão e o mouse

#game loop
def game_loop(janela, player=None):
    global dificuldade
    if not player:
        player = Player()
    g_bg = Sprite("assets/game_bg.jpg")
    g_bg.set_position((janela.width-g_bg.width)/2, (janela.height-g_bg.height)/2)
    shots = []
    timer = 0
    last_shot = -1
    last_enemy_shot = -1
    last_enemy_move = -1
    last_hit = -1
    direction = 0
    vel = janela.width
    enemy_move_delay = 1
    enemy_shot_delay = 3/dificuldade
    shot_delay = min(0.3*dificuldade, 1)
    hit_delay = 1
    matrix = EnemyMatrix(3 + dificuldade)
    while not kb.key_pressed("esc"):
        janela.set_background_color([0,0,0])
        g_bg.draw()
        if kb.key_pressed("right") or kb.key_pressed("d"):
            player.move_x(vel*janela.delta_time())
            if player.x + player.width > WIDTH:
                player.x = WIDTH - player.width
        if kb.key_pressed("left") or kb.key_pressed("a"):
            player.move_x(vel*janela.delta_time()*(-1))
            if player.x < 0:
                player.x = 0
        if kb.key_pressed("space"):
            if timer - last_shot >= shot_delay:
                last_shot = timer
                shots.append(Shot(player.x+player.width/2, player.y))
        if timer - last_enemy_shot >= enemy_shot_delay:
            last_enemy_shot = timer
            matrix.shoot(shots)
        if timer - last_enemy_move >= enemy_move_delay:
            last_enemy_move = timer
            direction = random.randint(-1,1)
        
        if matrix[0][0].x <= 0 or matrix[0][matrix.cols-1].x + matrix[0][matrix.cols-1].width >= WIDTH:
            direction *= -1

        dt = janela.delta_time()
        matrix.move(dt, direction)

        for shot in shots:
            shot.move(dt)
            #shot.update()
            shot.draw()
            if shot.y < 0 or shot.y > janela.height:
                shots.remove(shot)

        for shot in shots:
            if not shot.drawable:
                continue
            if shot.direction == 1:
                if  not (timer - last_hit >= hit_delay):
                    last_hit = timer
                    continue
                if Collision.collided_perfect(shot, player):
                    player.hit()
                    shot.hide()
                    if not player.drawable:
                        main(janela)
            else:
                matrix.collision(shot)

        if not matrix.alive:
            dificuldade += 1
            player.add_hp()
            game_loop(janela, player)
        player._draw_()
        matrix.draw()
        timer += janela.delta_time()
        janela.update()

#loop do menu de dificuldade
def settings_loop(janela):
    global dificuldade
    while not kb.key_pressed("esc"):
        if mouz.is_over_object(easy):
            easy.set_curr_frame(1)
            if mouz.is_button_pressed(1):
                dificuldade = 1
        else:
            easy.set_curr_frame(0)
        if mouz.is_over_object(normal):
            normal.set_curr_frame(1)
            if mouz.is_button_pressed(1):
                dificuldade = 2
        else:
            normal.set_curr_frame(0)
        if mouz.is_over_object(hard):
            hard.set_curr_frame(1)
            if mouz.is_button_pressed(1):
                dificuldade = 3
        else:
            hard.set_curr_frame(0)
        janela.set_background_color([0,0,0])
        sets_bg.draw()
        easy.draw()
        normal.draw()
        hard.draw()
        janela.update()

#globais
#janela, botões da interface, globais numéricas, teclado e mouse
janela = Window(WIDTH, HEIGHT)
janela.set_title("Invaders Must Die!")
jogar = Sprite("assets/jogar.png", 2)
settings = Sprite("assets/settings.png",2)
ranking = Sprite("assets/ranking.png",2)
exit = Sprite("assets/exit.png",2)
easy = Sprite("assets/easy.png",2)
normal = Sprite("assets/medium.png",2)
hard = Sprite("assets/hard.png",2)
bg = Sprite("assets/Level 5 Wonder Space.png")
sets_bg = Sprite("assets/settings_bg.png")

dificuldade = 1
padding = janela.width/6
centro = janela.width/2 - jogar.width/2
score = 0

kb = janela.get_keyboard()
mouz = janela.get_mouse()

#setagem
sets_bg.set_position((janela.width - sets_bg.width)/2, (janela.width - sets_bg.height)/2)
bg.set_position(janela.width/2 - bg.width/2, janela.height/2 - bg.height/2)
easy.set_position(centro, padding+(padding/2-jogar.height/2))
normal.set_position(centro, padding*2 +(padding/2-settings.height/2))
hard.set_position(centro, padding*3 + (padding/2-ranking.height/2))
jogar.set_position(centro, padding+(padding/2-jogar.height/2))
settings.set_position(centro, padding*2 +(padding/2-settings.height/2))
ranking.set_position(centro, padding*3 + (padding/2-ranking.height/2))
exit.set_position(centro, padding*4+ (padding/2-exit.height/2))

#main loop
def main(janela):
    while True:
        janela.set_background_color([0,0,20])
        if mouz.is_over_object(jogar):
            jogar.set_curr_frame(1)
            if mouz.is_button_pressed(1):
                game_loop(janela)
        else:
            jogar.set_curr_frame(0)
        if mouz.is_over_object(settings):
            settings.set_curr_frame(1)
            if mouz.is_button_pressed(1):
                settings_loop(janela)
        else:
            settings.set_curr_frame(0)
        if mouz.is_over_object(ranking):
            ranking.set_curr_frame(1)  
            if mouz.is_button_pressed(1):
                pass
        else:
            ranking.set_curr_frame(0)
        if mouz.is_over_object(exit):
            exit.set_curr_frame(1)
            if mouz.is_button_pressed(1):
                janela.close()
        else:
            exit.set_curr_frame(0)

        bg.draw()
        jogar.draw()
        settings.draw()
        ranking.draw()
        exit.draw()

        janela.update()

main(janela)

