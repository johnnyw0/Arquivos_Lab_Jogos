from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.mouse import*
import func2

def rank():


    #Resolução da janela e background
    janela = Window(564,772)
    janela.set_title('Space Invaders')
    bg = GameImage('pngteste/space.png')
    mouse = Window.get_mouse()



    #Sentinela que verifica se está no menu principal ou não
    out_menu = True

    lista_ord = func2.ordena_arq("ranking.txt")


    while out_menu:

        bg.draw()

        for i in range(len(lista_ord)):
            if i == 5: break
            janela.draw_text(f"{lista_ord[i][0]}: {lista_ord[i][1]}", janela.width/2 - 50, 200 + (i * 100), size=24, color=(255, 255, 255), font_name='Arial', bold=False, italic=False)

        janela.update()