from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from func import*

def jogo():

    #criando janela do jogo
    janela = Window(1280,720)
    janela.set_title('Space Invaders')
    bg = GameImage("png/space.png")
    out_menu = True
    teclado = Window.get_keyboard()

    #Nave e tiro
    nave = Sprite("png/nave.png")
    nave.x = (janela.width/2)-(nave.width/2)
    nave.y = janela.height-100
    tiros = []

    #Valores absolutos
    velD = 600
    velE = -600
    veltiro = 750
    recarga = 0.2

    while out_menu:

        bg.draw()
        nave.draw()

        #Movimentação da nave
        if teclado.key_pressed("right"):
            nave.move_x(velD*janela.delta_time())
        if teclado.key_pressed("left"):
            nave.move_x(velE*janela.delta_time())


        #Comando para atirar com tempo de recarga
        recarga += janela.delta_time()

        if teclado.key_pressed("space") and recarga > 0.2:
            tiros = atirar(nave, tiros)
            recarga = 0


        if tiros != []:
            for tiro in tiros:
                tiro.draw()
                tiro.y -= veltiro*janela.delta_time()

		

        out_menu = voltar_menu()
        janela.update()