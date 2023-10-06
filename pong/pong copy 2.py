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
bola = Sprite("png/bola2.png")
bola.set_position(((janela.width/2)-(bola.width/2)), (janela.height/2)-(bola.height/2))
bola2 = Sprite("png/bola.png")
bola2.set_position(((janela.width/2)-(bola.width/2)), (janela.height/2)-(bola.height/2))
padE = Sprite("png/pad.png")
padE.set_position(5, janela.height/2)
padD = Sprite("png/pad.png")
padD.set_position(janela.width-padD.width-5, janela.height/2)

#Valores absolutos
velx1 = vely1 = 350
velx2 = vely2 = -350
velPcima = -750
velPbaixo = 750
teclado = Window.get_keyboard()
Colidiu = False
Parou = False
espaco = False
pontosE = 0
pontosD = 0


#Gameloop
while True:
    #Movimento da bola
    bola.move_x(velx1*janela.delta_time())
    bola.move_y(vely1*janela.delta_time())
    bola2.move_x(velx2*janela.delta_time())
    bola2.move_y(vely2*janela.delta_time())

    if teclado.key_pressed("W"):
        padE.move_y(velPcima*janela.delta_time())
    if teclado.key_pressed("S"):
        padE.move_y(velPbaixo*janela.delta_time())

    if teclado.key_pressed("up"):
        padD.move_y(velPcima*janela.delta_time())
    if teclado.key_pressed("down"):
        padD.move_y(velPbaixo*janela.delta_time())

    if Collision.collided(bola, padE):
        bola.x = 5 + padE.width
        velx1 *= -1.1
    if Collision.collided(bola, padD):
        bola.x = janela.width - 5 - padD.width - bola.width
        velx1 *= -1.1

    if Collision.collided(bola2, padE):
        bola2.x = 5 + padE.width
        velx2 *= -1.1
    if Collision.collided(bola2, padD):
        bola2.x = janela.width - 5 - padD.width - bola2.width
        velx2 *= -1.1


    #Colisão com a parede de cima e de baixo
    if bola.y + bola.height >= janela.height:
        bola.y = janela.height - bola.height
        vely1 *= -1
    if bola.y < 0:
        bola.y = 0
        vely1 *= -1
    if bola2.y + bola2.height >= janela.height:
        bola2.y = janela.height - bola2.height
        vely2 *= -1
    if bola2.y < 0:
        bola2.y = 0
        vely2 *= -1
    if padE.y < 0:
        padE.y = 0
    if padE.y + padE.height > janela.height:
        padE.y = janela.height - padE.height
    if padD.y < 0:
        padD.y = 0
    if padD.y + padD.height > janela.height:
        padD.y = janela.height - padD.height

    #Pontuação
    if bola.x < 0:
        bola.set_position(((janela.width/2)-(bola.width/2)), (janela.height/2)-(bola.height/2))
        Colidiu = True
        Parou = True
        pontosD += 1
    if bola.x + bola.width > janela.width:
        bola.set_position(((janela.width/2)-(bola.width/2)), (janela.height/2)-(bola.height/2))
        Colidiu = True
        Parou = True
        pontosE += 1
    if bola2.x < 0:
        bola.set_position(((janela.width/2)-(bola.width/2)), (janela.height/2)-(bola.height/2))
        Colidiu = True
        Parou = True
        pontosD += 1
    if bola2.x + bola2.width > janela.width:
        bola.set_position(((janela.width/2)-(bola.width/2)), (janela.height/2)-(bola.height/2))
        Colidiu = True
        Parou = True
        pontosE += 1


    # soltou = True
    # #Recomeçar com bola no meio e usando espaço
    # if Colidiu and teclado.key_pressed("space"):
    #     soltou = False
    #     espaco = True
    
    # if Parou and soltou and espaco:
    #     Parou = False
    #     velx1 = vely = 500

    bg.draw()
    padD.draw()
    padE.draw()
    bola.draw()
    bola2.draw()
    janela.draw_text(f"{pontosE}:{pontosD}", janela.width/2, 0, size=40, color=(0,0,0), font_name='Arial', bold=False, italic=False)
    janela.update()