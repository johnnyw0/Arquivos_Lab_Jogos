from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.mouse import*


janela = Window(1280,720)
janela.set_title('João André Watanabe')
bg = GameImage('png/space.png')
play = GameImage('png/bola2.png')
play.set_position(janela.width/2-play.width/2, janela.height/2-play.height/2)
mouse = Window.get_mouse()




while True:

    if mouse.is_over_object(play):
        janela.close()





    bg.draw()
    play.draw()
    janela.update()