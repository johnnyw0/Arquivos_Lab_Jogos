from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from PPlay.collision import*
from func import*

def jogo():

    #criando janela do jogo
    janela = Window(564,772)
    janela.set_title('Space Invaders')
    bg = GameImage("pngteste/game_bg.jpg")
    out_menu = True
    teclado = Window.get_keyboard()

    #Nave e tiro
    nave = Sprite("pngteste/navi_smol.png")
    nave.x = (janela.width/2)-(nave.width/2)
    nave.y = janela.height-100
    tiros = []

    #Inimigos
    matriz_inimigos = []
    linhas = 3
    colunas = 5
    velIx = 100
    velIy = 30


    #Valores absolutos
    velD = 600
    velE = -600
    veltiro = 750
    recarga = 0.2
    status = True
    fps = 60
    pontos = 0
    clock = pygame.time.Clock()







    while out_menu:

        bg.draw()
        nave.draw()







        #Movimentação da nave
        if teclado.key_pressed("right"):
            nave.move_x(velD*janela.delta_time())
        if teclado.key_pressed("left"):
            nave.move_x(velE*janela.delta_time())
        if nave.x < 0:
            nave.x = 0
        if nave.x + nave.width > janela.width:
            nave.x = janela.width - nave.width








        #Comando para atirar com tempo de recarga
        recarga += janela.delta_time()

        if teclado.key_pressed("space") and recarga > 0.2:
            tiros = atirar(nave, tiros)
            recarga = 0

        if tiros != []:
            for tiro in tiros:
                tiro.draw()
                tiro.y -= veltiro*janela.delta_time()
		






        #Criando a matriz de inimigos
        if matriz_inimigos == []:

            matriz_inimigos = cria_mat(matriz_inimigos, linhas, colunas)

        if matriz_inimigos != []:

            # for i in range(linhas):
            #     for j in range(colunas):
            #         matriz_inimigos[i][j].draw()

            for linha in matriz_inimigos:
                for coluna in linha:
                    coluna.draw()

            matriz_inimigos, velIx, status = movimento_matriz(matriz_inimigos, velIx, velIy, nave, janela)

        if tiros != []:
            pontos = acerto_tiro(tiros, matriz_inimigos, pontos)






        if status == False:
            janela.close()

        clock.tick(fps)

        janela.draw_text(f"FPS: {fps}", 100, janela.height - 50, 10, (255,255,255), "Arial")
        janela.draw_text(f"Pontuação: {pontos}", 100, janela.height - 40, 10, (255,255,255), "Arial")

        out_menu = voltar_menu()
        janela.update()