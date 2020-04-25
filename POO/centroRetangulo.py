'''programa que usa os conceitos de classes, associações e funções. Atraves do vértice inferior esquerdo (utilizando somente o primeiro quadrante)'''
class Ponto(object):
	def __init__(self, px = 0, py = 0):
		self.x = px
		self.y = py
	
class Retangulo(object):
	def __init__(self, base, altura, ponto):
		self.h = altura
		self.b = base
		self.vertice = ponto
	
def mostraPonto(ponto):
	print(ponto.x, ponto.y)

def encontraCentroRetangulo(retangulo):
	ponto = Ponto()
	ponto.x = (retangulo.vertice.x + retangulo.b)/2
	ponto.y = (retangulo.vertice.y + retangulo.h)/2
	return ponto

def main():
	entrada = input('Digite o ponto do vértice inferior esquerdo do retangulo (x,y) :')
	x, y = (float(pn) for pn in entrada.split(','))
	p = Ponto(x, y)
	entrada = input('Digite a base e a altura do retangulo (b,h) :')
	base, altura = (float(pn) for pn in entrada.split(','))
	r = Retangulo(base, altura, p)
	centro_r = encontraCentroRetangulo(r)
	print('O centro do retangulo é')
	mostraPonto(centro_r)
		

if __name__ == '__main__':
	main()
