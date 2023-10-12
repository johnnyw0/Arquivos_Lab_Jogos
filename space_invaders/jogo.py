from PPlay.window import*
import func

def jogo():

    #criando janela do jogo
    janela = Window(1280,720)
    janela.set_title('Space Invaders')
    out_menu = True

    while out_menu:

        out_menu = func.voltar_menu()



        janela.update()