from PPlay.window import*
from PPlay.sprite import*

janela = Window(1280,720)
janela.set_title('Space Invaders')
teclado = Window.get_keyboard()

def voltar_menu():
    return False if teclado.key_pressed("esc") else True


def atirar(nave, lista):


    bala = Sprite("png/bola2.png")
    bala.x = nave.x + nave.width/2
    bala.y = nave.y - bala.height

    lista.append(bala)

    return lista
