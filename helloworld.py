from PPlay.window import*

janela = Window(200,200)
janela.set_title('João André Campos Watanabe')
janela.delay(3000)

janela.draw_text('Hello World', 0, 0, size=12, color=(0,0,0), font_name='Arial', bold=False, italic=False)
janela.update()