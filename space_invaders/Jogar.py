from PPlay.window import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.keyboard import*
from PPlay.gameimage import *

import random



def cria_matriz(matriz, linhas, colunas):
	
	for l in range(linhas):
		coluna = []
		for c in range(colunas):
			alien = Sprite("aliensprite.png", 1)
				
			alien.x = (alien.width + alien.width / 2) * c 
			alien.y = (alien.height + alien.height / 2)  * l
			coluna.append(alien)

		matriz.append(coluna)
	
	return matriz

def movimento_aliens(matriz, velX, velY, nave, tela):
    
    colisao_base = False
    
    for linha in matriz:
        for alien in linha:
            alien.move_x(velX * tela.delta_time())
            if (alien.x <= 5):
                alien.x = 5
                velX *= -1
                for linha in matriz:
                    for alien in linha:
                        alien.move_y(velY)
            elif(alien.x + alien.width + 5 >= tela.width):
                alien.x = tela.width - (alien.width + 5)
                velX *= -1
                for linha in matriz:
                    for alien in linha:
                        alien.move_y(velY)
            if (alien.y + alien.height >= nave.y):
                colisao_base = True
    
    return matriz, velX, colisao_base

def colisao_aliens(matriz, tiros):
    cont = 0
    for lin in matriz:
        for alien in lin:
            for tiro in tiros:
                if Collision.collided(tiro, alien):
                    lin.remove(alien)
                    tiros.remove(tiro)  
                    cont += 1
        if(lin == []): matriz.remove(lin)
            
    return cont

# inicializando a função "jogar".
def jogar():

    # definindo as dimensões da tela
    largura = 720
    altura = 640

    tela = Window(largura, altura)
    
    # velocidade da nave
    vel_n = 200
    
    # título da tela de gameplay da nave
    tela.set_title("Space Invaders")
    
    # PPLay reconhecendo as teclas apertadas
    teclado = Window.get_keyboard()
    
    # sprites utilizados
    nave = Sprite("sprite_ship_3.png")

    centro = largura/2 - nave.width/2
    # coordenadas da nave
    nave.x = centro
    nave.y = 540
    
    
    # estabelecendo o "cooldown" dos tiros e criando-os
    tiros = []
    cont = 1

    tiros_aliens = []
    cont_aliens = 0
    
    # criação da matriz de monstros
    matriz_aliens = []

    vidas = 3
    invisivel = False
    inv_cont = 0
    
    linhas = 3
    colunas = 3
    velX = 100
    velY = 15

    pontuacao = 0
    
    while True:
        cont += tela.delta_time()
        
        tela.set_background_color((0, 0, 0))
        
        # condições de criação dos tiros 
        if (teclado.key_pressed("SPACE") and (cont >= 0.25)):
            balas = Sprite("Tiro_Laser_Space_Invaders22.png")
            tiros.append(balas)
            balas.set_position(nave.x + nave.width//2 - 5, 530)
            cont = 0
        # 
        for balas in tiros:
            balas.move_y(-400 * tela.delta_time()) 
            if balas.y <= (-1) * balas.height:
                tiros.remove(balas)


        tela.set_background_color((0, 0, 0))

        if (teclado.key_pressed("left")):
            nave.x -= vel_n *tela.delta_time()

        if (teclado.key_pressed("right")):
            nave.x += vel_n *tela.delta_time()

        if (nave.x <= 0):
            nave.x = 0
        if (nave.x + nave.width >= tela.width):
            nave.x = tela.width - nave.width
        
        #SEÇÃO PARA CRIAR MATRIZ DE MONSTROS
		#cria a matriz se ela estiver vazia

        if (not matriz_aliens):
            matriz_aliens = cria_matriz(matriz_aliens, linhas, colunas)
			
        else:
            matriz_aliens, velX, fim = movimento_aliens(matriz_aliens, velX, velY, nave, tela)
            if(fim): break

            pontuacao += colisao_aliens(matriz_aliens, tiros)
            
            for linha in matriz_aliens:
                for coluna in linha:
                    coluna.draw()

            if cont_aliens >= 1:
                i = random.randint(0, len(matriz_aliens) - 1)
                j = random.randint(0, len(matriz_aliens[i]) - 1)

                alien_escolhido = matriz_aliens[i][j]
                tiro_alien = Sprite("Tiro_Laser_Space_Invaders22.png")
                tiro_alien.set_position(alien_escolhido.x + alien_escolhido.width/2, alien_escolhido.y + alien_escolhido.height)
                tiros_aliens.append(tiro_alien)
                cont_aliens = 0

        cont_aliens += tela.delta_time()

        for tiro in tiros_aliens:
            if(Collision.collided(nave, tiro) and not invisivel):
                vidas -= 1
                tiros_aliens.remove(tiro)

                nave = Sprite("sprite_ship_inv.png")
                nave.x = centro
                nave.y = 540
    
                nave.x = centro
                invisivel = True
                continue

            tiro.move_y(300 * tela.delta_time()) 
            if tiro.y >= altura + tiro.height:
                tiros_aliens.remove(tiro)

        

                
                    

        if(invisivel):
            inv_cont += tela.delta_time()
            if(inv_cont) >= 2:
                inv_cont = 0
                invisivel = False
                posicao = nave.x
                nave = Sprite("sprite_ship_3.png")
                nave.x = posicao
                nave.y = 540
    
        if(vidas == 0): break
        

        for tiro_alien in tiros_aliens:
            tiro_alien.draw()
        
        for tiro in tiros:
            tiro.draw()
        nave.draw()
        
        fps = 1/tela.delta_time() if tela.delta_time() > 0 else 0
        if(fps != 0):
            tela.draw_text(f"FPS: {int(fps)}", 5, 5, size=12, color=(255, 255, 255), font_name="Arial", bold=False, italic=False)

        tela.draw_text(f"Pontuação: {pontuacao}", 5, 15, size=12, color=(255, 255, 255), font_name="Arial", bold=False, italic=False)

        tela.draw_text(f"Vidas: {vidas}", 5, 25, size=12, color=(255, 255, 255), font_name="Arial", bold=False, italic=False)        
        tela.update()

