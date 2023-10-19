from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.mouse import*
import jogo
import dificuldade


#Resolução da janela e background
janela = Window(1280,720)
janela.set_title('Space Invaders')
bg = GameImage('png/space.png')

#Botões e título do jogo que estão no menu            
title = GameImage('png/title.png')
title.set_position(janela.width/2-title.width/2, 100)   #O título é espaçado de 100 pixels do começo da janela, o botão de jogar é espaçado 150 pixels do título
play = GameImage('png/play.png')                        #e os botões tem espaçamento de 100 pixels entre si
play.set_position(janela.width/2-play.width/2, 250)
dif = GameImage('png/dif.png')
dif.set_position(janela.width/2-dif.width/2, 350)
rank = GameImage('png/rank.png')
rank.set_position(janela.width/2-rank.width/2, 450)
exit = GameImage('png/exit.png')
exit.set_position(janela.width/2-exit.width/2, 550)


#Destaque nos botões
d_exit = GameImage('png/dexit.png')
d_exit.set_position(janela.width/2-d_exit.width/2, 550)
ddif = GameImage('png/ddif.png')
ddif.set_position(janela.width/2-dif.width/2, 350)
dplay = GameImage('png/dplay.png')
dplay.set_position(janela.width/2-play.width/2, 250)
drank = GameImage('png/drank.png')
drank.set_position(janela.width/2-rank.width/2, 450)


#Mouse e teclado
mouse = Window.get_mouse()
teclado = Window.get_keyboard()

#Sentinelas para definir as telas
i_menu = True


#Gameloop
while i_menu:

    bg.draw()
    dif.draw()
    rank.draw()
    title.draw()
    exit.draw()
    play.draw()


    #Destaque e efeitos dos botões
    if mouse.is_over_object(exit):
        d_exit.draw()

        if mouse.is_button_pressed(1):
            janela.close()

    if mouse.is_over_object(rank):
        drank.draw()

    if mouse.is_over_object(dif):
        ddif.draw()

        if mouse.is_button_pressed(1):
            dificuldade.diff()

    if mouse.is_over_object(play):
        dplay.draw()

        if mouse.is_button_pressed(1):
            jogo.jogo()


    janela.update()