from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.mouse import*
import func

def diff():


    #Resolução da janela e background
    janela = Window(1280,720)
    janela.set_title('Space Invaders')
    bg = GameImage('png/space.png')
    mouse = Window.get_mouse()


    #Botões e título do jogo que estão no menu
    title = GameImage('png/title.png')
    title.set_position(janela.width/2-title.width/2, 100)
    easy = GameImage('png/easy.png')                        
    easy.set_position(janela.width/2-easy.width/2, 250)
    medium = GameImage('png/medium.png')
    medium.set_position(janela.width/2-medium.width/2, 350)
    hard = GameImage('png/hard.png')
    hard.set_position(janela.width/2-hard.width/2, 450)


    deasy = GameImage('png/deasy.png')                        
    deasy.set_position(janela.width/2-deasy.width/2, 250)
    dmedium = GameImage('png/dmedium.png')
    dmedium.set_position(janela.width/2-dmedium.width/2, 350)
    dhard = GameImage('png/dhard.png')
    dhard.set_position(janela.width/2-dhard.width/2, 450)

    #Sentinela que verifica se está no menu principal ou não
    out_menu = True


    while out_menu:

        bg.draw()
        title.draw()
        easy.draw()
        medium.draw()
        hard.draw()


        #Destaque e efeitos dos botões
        if mouse.is_over_object(easy):
            deasy.draw()

        if mouse.is_over_object(medium):
            dmedium.draw()

        if mouse.is_over_object(hard):
            dhard.draw()

        #Voltar para o menu com ESC
        out_menu = func.voltar_menu()



        janela.update()