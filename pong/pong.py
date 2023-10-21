from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from PPlay.collision import*

#Janela e background
janela = Window(1200, 700)
janela.set_title("João André Watanabe")
janela.set_background_color([255,255,255])
bg = GameImage("png/fundo.png")
bg.set_position(0, 0)

#Game Objects
bola = Sprite("png/circle-16.png")
bola.set_position(((janela.width/2)-(bola.width/2)), (janela.height/2)-(bola.height/2))
padE = Sprite("png/pad.png")
padE.set_position(5, janela.height/2)
padD = Sprite("png/pad.png")
padD.set_position(janela.width-padD.width-5, janela.height/2)

#Valores absolutos
velx = vely = 350
velPcima = -350
velPbaixo = 350
teclado = Window.get_keyboard()
Colidiu = False
pontosE = 0
pontosD = 0


#Gameloop
while True:
    #Movimento da bola
    bola.move_x(velx*janela.delta_time())
    bola.move_y(vely*janela.delta_time())


        #Movimento do Pad
    if teclado.key_pressed("W"):
            padE.move_y(velPcima*janela.delta_time())
    if teclado.key_pressed("S"):
        padE.move_y(velPbaixo*janela.delta_time())


        #caso tenha P2
    if teclado.key_pressed("up"):
        padD.move_y(velPcima*janela.delta_time())
    if teclado.key_pressed("down"):
        padD.move_y(velPbaixo*janela.delta_time())

        #Colisão da bola com os Pads
    if Collision.collided(bola, padE):
        bola.x = 5 + padE.width
        velx *= -1.04
    if Collision.collided(bola, padD):
        bola.x = janela.width - 5 - padD.width - bola.width
        velx *= -1.04


    #Colisão da bola e dos Pads com a parede
    if bola.y + bola.height >= janela.height:
        bola.y = janela.height - bola.height
        vely *= -1
    if bola.y < 0:
        bola.y = 0
        vely *= -1
    if padE.y < 0:
        padE.y = 0
    if padE.y + padE.height > janela.height:
        padE.y = janela.height - padE.height
    if padD.y < 0:
        padD.y = 0
    if padD.y + padD.height > janela.height:
        padD.y = janela.height - padD.height


    #     #IA do pad direito
    # if bola.x > janela.width/2 and bola.y < padD.y and velx > 0:
    #     padD.move_y(velPcima*janela.delta_time())
    # if bola.x > janela.width/2 and bola.y > padD.y and velx > 0:
    #     padD.move_y(velPbaixo*janela.delta_time())

    #     #IA do pad esquerdo
    # if bola.x < janela.width/2 and bola.y < padE.y and velx < 0:
    #     padE.move_y(velPcima*janela.delta_time())
    # if bola.x < janela.width/2 and bola.y > padE.y and velx < 0:
    #     padE.move_y(velPbaixo*janela.delta_time())

    #Pontuação e retorno da bola para o centro
    if bola.x < 0:
        velx = vely = 0
        bola.set_position(((janela.width/2)-(bola.width/2)), (janela.height/2)-(bola.height/2))
        Colidiu = True
        pontosD += 1
    if bola.x + bola.width > janela.width:
        velx = vely = 0
        bola.set_position(((janela.width/2)-(bola.width/2)), (janela.height/2)-(bola.height/2))
        Colidiu = True
        pontosE += 1


    #Recomeçar com bola no meio e usando espaço
    if Colidiu and teclado.key_pressed("space"):
        velx = vely = 350

    bg.draw()
    padD.draw()
    padE.draw()
    bola.draw()
    janela.draw_text(f"{pontosE}:{pontosD}", janela.width/2, 0, size=40, color=(0,0,0), font_name='Arial', bold=False, italic=False)
    janela.update()