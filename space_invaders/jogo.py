from PPlay.window import*
from PPlay.sprite import*
from PPlay.gameimage import*
from PPlay.keyboard import*
from PPlay.collision import*
from func import*
import random

def jogo():

    #criando janela do jogo
    janela = Window(564,772)
    janela.set_title('Space Invaders')
    bg = GameImage("pngteste/game_bg.jpg")
    out_menu = True
    teclado = Window.get_keyboard()

    #Nave e tiro
    nave = Sprite("pngteste/nave.png")
    nave.x = (janela.width/2)-(nave.width/2)
    nave.y = janela.height-100
    tiros = []
    cronometro = 0
    limite_inv = 2

    #Inimigos
    matriz_inimigos = []
    tiros_inimigos = []
    linhas = 4
    colunas = 5 
    velIx = 100
    velIy = 30


    #Valores absolutos
    velD = 600
    velE = -600
    veltiro = 400
    recarga = 0.5
    status = True
    inv = False
    fps = 60
    pontos = 0
    vida = 3
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

        if teclado.key_pressed("space") and recarga > 0.5:
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

            matriz_aliens, velX, fim = movimento_aliens(matriz_aliens, velIx, velIy, nave, janela)

            for linha in matriz_inimigos:
                for coluna in linha:
                    coluna.draw()

            if recarga > 0.5:    
                i = random.randint(0, len(matriz_inimigos) - 1)
                j = random.randint(0, len(matriz_inimigos[i]) - 1)
                

                alien_esc = matriz_inimigos[i][j]
                tiro = Sprite("pngteste/shot_enemy.png")
                tiro.x = alien_esc.x + alien_esc.width/2
                tiro.y = alien_esc.y + alien_esc.height
                tiros_inimigos.append(tiro)
                recarga = 0


            cronometro += janela.delta_time()
            if tiros_inimigos != []:

                for tiro in tiros_inimigos:
                    tiro.draw()
                    tiro.y += veltiro*janela.delta_time()
                    if Collision.collided(tiro, nave) and not inv:
                        vida -= 1
                        nave = Sprite("pngteste/nave2.png")
                        nave.x = (janela.width/2)-(nave.width/2)
                        nave.y = janela.height-100
                        tiros_inimigos.remove(tiro)
                        inv = True
                        cronometro = 0


            if cronometro > limite_inv and inv:
                inv = False
                x = nave.x
                y = nave.y
                nave = Sprite("pngteste/nave.png")
                nave.set_position(x, y)
                

        if tiros != []:
            pontos = acerto_tiro(tiros, matriz_inimigos, pontos)



        if status == False:
            break

        if vida == 0:
            break

        clock.tick(fps)

        janela.draw_text(f"FPS: {fps}", 100, janela.height - 50, 10, (255,255,255), "Arial")
        janela.draw_text(f"Pontuação: {pontos}", 100, janela.height - 40, 10, (255,255,255), "Arial")

        out_menu = voltar_menu()
        janela.update()