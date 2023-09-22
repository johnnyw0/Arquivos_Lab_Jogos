from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*

janela = Window(1200, 700)
janela.set_title("João André Watanabe")
janela.set_background_color([255,255,255])

bg = GameImage("png/fundo.png")
bg.set_position(0, 0)
bola = Sprite("png/bola.png")
bola.set_position((janela.height/2)+200, (janela.width/2)-250)

velx = vely = 500

while True:
    bola.move_x(velx*janela.delta_time())
    bola.move_y(vely*janela.delta_time())


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

    bg.draw()
    bola.draw()
    janela.update()