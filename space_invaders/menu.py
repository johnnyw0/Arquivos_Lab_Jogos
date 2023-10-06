from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*

janela = Window(1280,720)
janela.set_title('João André Watanabe')
bg = GameImage('png/space.png')

while True:
    bg.draw()
    janela.update()