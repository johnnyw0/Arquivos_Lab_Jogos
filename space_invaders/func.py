from PPlay.window import*

janela = Window(1280,720)
janela.set_title('Space Invaders')
teclado = Window.get_keyboard()

def voltar_menu():
    return False if teclado.key_pressed("esc") else True