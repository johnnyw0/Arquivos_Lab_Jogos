from PPlay.window import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.keyboard import*
from PPlay.gameimage import *
from func2 import *
import random

# inicializando a função "jogar".
def jogar():




    # definindo as dimensões da janela
    largura = 564
    altura = 772
    janela = Window(largura, altura)
    janela.set_title("Space Invaders")
    bg = GameImage("pngteste/game_bg.jpg")
    teclado = Window.get_keyboard()
    



    #Nave e Tiro
    nave = Sprite("pngteste/nave.png")
    nave.x = (janela.width/2)-(nave.width/2)
    nave.y = janela.height-100
    tiros = []

    
    #tiros

    
    # Inimigos
    matriz_inimigos = []
    tiros_aliens = []
    inv = False
    inv_cont = 0
    linhas = 5
    colunas = 5



    # Valores absolutos
    vel_n = 600
    velX = 100
    velY = 15
    clock = pygame.time.Clock()
    fps = 60
    vidas = 3
    recarga = 1
    rec_inimigo = 0
    c_base = False






    pontuacao = 0
    
    while True:
        
        bg.draw()        
        nave.draw()

        # condições de criação dos tiros 
        recarga += janela.delta_time()
        if (teclado.key_pressed("SPACE") and (recarga >= 0.25)):
            balas = Sprite("pngteste/shot.png")
            tiros.append(balas)
            balas.set_position(nave.x + nave.width//2 - 5, 530)
            recarga = 0
        # 
        for balas in tiros:
            balas.move_y(-400 * janela.delta_time()) 
            if balas.y <= (-1) * balas.height:
                tiros.remove(balas)



        if (teclado.key_pressed("left")):
            nave.x -= vel_n *janela.delta_time()

        if (teclado.key_pressed("right")):
            nave.x += vel_n *janela.delta_time()

        if (nave.x <= 0):
            nave.x = 0
        if (nave.x + nave.width >= janela.width):
            nave.x = janela.width - nave.width
        
        #SEÇÃO PARA CRIAR MATRIZ DE MONSTROS
		#cria a matriz se ela estiver vazia

        if (not matriz_inimigos):
            matriz_inimigos = cria_matriz(matriz_inimigos, linhas, colunas)
			
        else:
            matriz_inimigos, velX, c_base = movimento_aliens(matriz_inimigos, velX, velY, nave, janela)

            pontuacao += colisao_aliens(matriz_inimigos, tiros)
            
            for linha in matriz_inimigos:
                for coluna in linha:
                    coluna.draw()

            if rec_inimigo >= 1:
                i = random.randint(0, len(matriz_inimigos) - 1)
                j = random.randint(0, len(matriz_inimigos[i]) - 1)

                alien_escolhido = matriz_inimigos[i][j]
                tiro_alien = Sprite("pngteste/shot.png")
                tiro_alien.set_position(alien_escolhido.x + alien_escolhido.width/2, alien_escolhido.y + alien_escolhido.height)
                tiros_aliens.append(tiro_alien)
                rec_inimigo = 0

        rec_inimigo += janela.delta_time()

        for tiro in tiros_aliens:
            if(Collision.collided(nave, tiro) and not inv):
                vidas -= 1
                tiros_aliens.remove(tiro)

                nave = Sprite("pngteste/nave2.png")
                nave.x = (janela.width/2 - nave.width/2)
                nave.y = janela.height - 100
    
                inv = True
                continue

            tiro.move_y(300 * janela.delta_time()) 
            if tiro.y >= altura + tiro.height:
                tiros_aliens.remove(tiro)


        if(inv):
            inv_cont += janela.delta_time()
            if(inv_cont) >= 2:
                inv_cont = 0
                inv = False
                posicao = nave.x
                nave = Sprite("pngteste/nave.png")
                nave.x = posicao
                nave.y = janela.height - 100
    
        if(vidas == 0 or c_base == True):
            nome = input("Qual seu nome?: ")
            arq = open("ranking.txt", 'w')

            arq.write(f"{nome}: {pontuacao}")
            break

        

        for tiro_alien in tiros_aliens:
            tiro_alien.draw()
        
        for tiro in tiros:
            tiro.draw()
        

        clock.tick(fps)

        janela.draw_text(f"FPS: {int(fps)}", janela.width -55, 5, size=12, color=(255, 255, 255), font_name="Arial", bold=False, italic=False)

        janela.draw_text(f"Pontuação: {pontuacao}", 5, 15, size=24, color=(255, 255, 255), font_name="Arial", bold=False, italic=False)

        janela.draw_text(f"Vidas: {vidas}", 5, 38, size=24, color=(255, 255, 255), font_name="Arial", bold=False, italic=False)        
        janela.update()

