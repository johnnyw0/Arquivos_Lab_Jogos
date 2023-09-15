import pygame
from PPlay.window import*
from PPlay.sprite import*

janela = Window(1200, 700)
janela.set_title("João André Watanabe")
janela.set_background_color([255,255,255])


bola = Sprite("circle-16.png")
bola.set_position((janela.height/2)+200, (janela.width/2)-250)
bola.draw()

while True:
    janela.update()
