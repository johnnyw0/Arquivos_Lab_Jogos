from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.collision import*

janela = Window(1200, 700)
janela.set_title("João André Watanabe")
janela.set_background_color([255,255,255])

bg = GameImage("png/fundo.png")
bg.set_position(0, 0)
bola = Sprite("png/bola.png")
bola.set_position((janela.height/2)+200, (janela.width/2)-250)

bola2 = Sprite("png/bola.png")
bola2.set_position((janela.height)-200, (janela.width)-250)

velx = vely = 300
velx2 = vely2 = 500

while True:
    bola.move_x(velx*janela.delta_time())
    bola.move_y(vely*janela.delta_time())
    bola2.move_x(velx2*janela.delta_time())
    bola2.move_y(vely2*janela.delta_time())

    if bola.x + bola.width >= janela.width:
        bola.x = janela.width - bola.width
        velx *= -1
    if bola.x < 0:
        bola.x = 0
        velx *= -1
    if bola.y + bola.height >= janela.height:
        bola.y = janela.height - bola.height
        vely *= -1
    if bola.y < 0:
        bola.y = 0
        vely *= -1

    if Collision.collided(bola, bola2):

        velx2 *= -1.2
        vely2 *= -1.2

    if bola2.x + bola2.width >= janela.width:
        bola2.x = janela.width - bola2.width
        velx2 *= -1
    if bola2.x < 0:
        bola2.x = 0
        velx2 *= -1
    if bola2.y + bola2.height >= janela.height:
        bola2.y = janela.height - bola2.height
        vely2 *= -1
    if bola2.y < 0:
        bola2.y = 0
        vely2 *= -1

#jbbhhbh
    bola.draw()
    bola2.draw()
    janela.update()