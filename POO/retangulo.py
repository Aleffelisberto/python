'''Criando uma classe que representa um retangulo. O programa basicamente cria um local(usando um objeto da classe retangulo), e com o tamanho padrão de pisos dado, calcula o número de pisos necessários para a pavimentação do local'''
class Retangulo(object):
	def __init__(self, base = 0, altura = 0):
		self.b = base
		self.h = altura
	def mudaValorLados(self, base, altura):
		self.b = base
		self.h = altura
	def getValorLados(self):
		return tuple((self.b, self.h))
	def calculaArea(self):
		print('A area é %.2f' %(self.b * self.h))
		return float(self.b * self.h)
	def calculaPerimetro(self):
		print('O perímetro é %.2f' %((self.b * 2) + (self.h * 2)))
		return float(((self.b * 2) + (self.h * 2)))

def main():
	lados = input('Digite a base e a altura respectivamente do local a ser criado: ')
	baseLocal, alturaLocal = (float(numero) for numero in lados.split(' '))
	local = Retangulo(baseLocal, alturaLocal)
	lados = input('Agora digite a base e a altura do piso padrão para a pavimentação do local: ')
	basePiso, alturaPiso = (float(numero) for numero in lados.split(' '))
	piso = Retangulo(basePiso, alturaPiso)
	print('Os lados do local são', local.getValorLados(), sep=' ')
	print('Os lados do piso são', piso.getValorLados(), sep=' ')
	perimetroLocal = local.calculaPerimetro()
	areaLocal = local.calculaArea()
	perimetroPiso = piso.calculaPerimetro()
	areaPiso = piso.calculaArea()
	print('Serão necessários %i pisos para a pavimentação do local' %((areaLocal // areaPiso) + 1))


if __name__ == "__main__":
	main()
