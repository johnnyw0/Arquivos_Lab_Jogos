from PPlay.window import*
from PPlay.sprite import*
from PPlay.collision import*
import random



def ordena_arq(arquivo):
    arq = open(arquivo, 'r')

    linhas = arq.readlines()
    pessoas = []
    for linha in linhas:
        pessoa = linha.split()
        pessoas.append((pessoa[0], int(pessoa[1])))

    pessoas.sort(key=lambda pessoa: pessoa[1], reverse=True)

    return pessoas

def cria_matriz(matriz, linhas, colunas):
	
	for l in range(linhas):
		coluna = []
		for c in range(colunas):
			alien = Sprite("pngteste/alien.png", 1)
				
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
            if (alien.x < 5):
                alien.x = 5
                velX *= -1
                for linha in matriz:
                    for alien in linha:
                        alien.y += velY
            elif(alien.x + alien.width + 5 > tela.width):
                alien.x = tela.width - (alien.width + 5)
                velX *= -1
                for linha in matriz:
                    for alien in linha:
                        alien.y += velY
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
                    cont += 25
        if(lin == []): matriz.remove(lin)
            
    return cont