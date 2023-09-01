from PPlay.window import*

janela = Window(800,500)
janela.set_title('João André Campos Watanabe')
janela.draw_text('Hello World', 110, 220, size=20, color=(255,255,255), font_name='Arial', bold=False, italic=False)
janela.update()
janela.delay(3000)