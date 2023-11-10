from PPlay.window import*
from PPlay.sprite import*

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