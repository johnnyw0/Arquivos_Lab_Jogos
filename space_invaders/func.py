from PPlay.window import*
from PPlay.sprite import*
import random

janela = Window(1280,720)
janela.set_title('Space Invaders')
teclado = Window.get_keyboard()


#Função para voltar ao menu
def voltar_menu():
    return False if teclado.key_pressed("esc") else True

#Função de atirar
def atirar(nave, lista):

    bala = Sprite("pngteste/shot.png")
    bala.x = nave.x + nave.width/2
    bala.y = nave.y - bala.height

    lista.append(bala)

    return lista



#Criar inimigos
def cria_mat(matriz, lin, col):

	for l in range(lin):
		linhas = []
		for c in range(col):
			alien = Sprite("pngteste/alien.png")	
			alien.x = (alien.width + alien.width / 2) * c + 10
			alien.y = (alien.height + alien.height / 2)  * l
			linhas.append(alien)

		matriz.append(linhas)
	
	return matriz


#Tiro do monstro

# def tiro_monstro(lista, alien):

# 	tiro = Sprite("pngteste/shot_enemy.png")
# 	tiro.x = alien.x + alien.width/2
# 	tiro.y = alien.y + alien.height

# 	lista.append(tiro)

# 	return lista





#Movimento da matriz de inimigos
def colisao_matriz(matriz, velX, nave, janela):
	
	lateral = False
	base = True
	
	for linha in matriz:
		for alien in linha:
			alien.x += velX * janela.delta_time()
			if (alien.x <= 5 or alien.x + alien.width + 5 >= janela.width):
				lateral = True
			if (alien.y + alien.height >= nave.y):
				base = False
	
	return lateral, base

def movimento_matriz(matriz, velX, velY, nave, janela):

	c_lateral, c_base = colisao_matriz(matriz, velX, nave, janela)
			
	if (c_lateral == True):
		velX *= -1
		for linha in matriz:
			for alien in linha: 
				alien.y += velY
	
	return matriz, velX, c_base


def limites_matriz(lista_de_aliens):

	listaX = []
	listaY = []
	
	for linha in lista_de_aliens:
		for alien in linha:
		
			listaX.append(alien.x)
			listaY.append(alien.y)
	
	minX = min(listaX)
	maxX = max(listaX) + lista_de_aliens[0][0].x
	minY = min(listaY)
	maxY = max(listaY) + lista_de_aliens[0][0].y
	
	return minX, maxX, minY, maxY
		
		
#tiro da nave no monstro
def acerto_tiro(lista_de_tiros, lista_de_aliens, pontos):
	
	minX, maxX, minY, maxY = limites_matriz(lista_de_aliens)
	
	for tiro in lista_de_tiros:
		
		if (tiro.x >= minX and tiro.x <= maxX) and (tiro.y >= minY and tiro.y <= maxY):
			for i in range(len(lista_de_aliens) - 1, -1, -1):
				
				if (lista_de_aliens[i] != []):
					minX, maxX, minY, maxY = limites_matriz(lista_de_aliens)
					
					for alien in lista_de_aliens[i]:
					
						if (tiro.collided(alien) and (tiro in lista_de_tiros)):
							lista_de_tiros.remove(tiro)
							pontos += 25
							
							if (alien.total_frames == 1):
								lista_de_aliens[i].remove(alien)
								

				if (lista_de_aliens[i] == []):
					lista_de_aliens.pop(i)
					
				

	return pontos