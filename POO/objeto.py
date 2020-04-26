import math

class ObjetoGrafico(object):
        def __init__(self, cor_preenchimento, preenxida, cor_contorno):
                self.background = cor_preenchimento
                self.filled = preenxida
                self.outlinecolor = cor_contorno

class Retangulo(ObjetoGrafico):
        def __init__(self, cor_preenchimento, preenxida, cor_contorno, base, alt):
                super(Retangulo, self).__init__(cor_preenchimento, preenxida, cor_contorno)
                self.b = base
                self.h = alt
        def calcArea(self):
                print("A área do retangulo é", self.b * self.h, sep= " ")
        def calcPerimetro(self):
                print("O perímetro do retangulo é", self.b*2 + self.h*2, sep=" ")

class Circulo(ObjetoGrafico):
        def __init__(self, cor_preenchimento, preenxida, cor_contorno, raio):
                super(Circulo, self).__init__(cor_preenchimento, preenxida, cor_contorno)
                self.r = raio
        def calcArea(self):
                print("A área do circulo é", math.pi * math.pow(self.r, 2), sep=" ")
        def calcPerimetro(self):
                print('O perímetro do círculo é', 2 * math.pi * self.r, sep=" ")

class Triangulo(ObjetoGrafico):
        def __init__(self, cor_preenchimento, preenxida, cor_contorno, base, alt):
                super(Triangulo, self).__init__(cor_preenchimento, preenxida, cor_contorno)
                self.b = base
                self.h = alt
        def calcArea(self):
                print("A área do triângulo é", (self.b * self.h) / 2, sep=" ")
        def calcPerimetro(self):
                lado = math.sqrt(math.pow((self.b / 2), 2) + math.pow(self.h, 2))
                print('O perímetro do triângulo é', ((lado * 2) + self.b), sep=" ")

def main():
	plano = ObjetoGrafico('branco', True, 'preto')
	retangulo = Retangulo('branco', False, 'vermelho', 10, 12)
	retangulo.calcArea()
	retangulo.calcPerimetro()
	circulo = Circulo('branco', False, 'vermelho', 10)
	circulo.calcArea()
	circulo.calcPerimetro()
	triangulo = Triangulo('branco', False, 'vermelho', 5, 8)
	triangulo.calcArea()
	triangulo.calcPerimetro()

if __name__ == '__main__':
	main()
