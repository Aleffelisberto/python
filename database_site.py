"""
Programa que simula um database de sites. È apenas um simples código para estudo de exceções, statements, database, classes e arquivos
O programa é apenas a fins de estudo, não leve em conta erros como nome de sites, urls etc
"""

import dbm

class Sites(object):
	"""
	Classe que organiza um banco de dados de sites
	"""
	__sites_database = dbm.open('database', 'c')

	def __init__(self, f=''):
		try:
			self.__sites = open(f, 'a+')
			for lines in self.__sites.readlines():
				site_name, site_url = lines.split(' ')
				__sites_database[site_name] = site_url
		except FileNotFoundError:
			print('Houve um erro na abertura de {}'.format(f))
		finally:
			pass
	
	def addSite(self, nome, url):
		if(Sites.isSiteValid(url)):
			if nome.lower().encode() in Sites.__sites_database.keys():
				print('O site ja existe no banco de dados!')
			else:
				Sites.__sites_database.setdefault(nome.lower(), url)
				self.__sites.write('{} {}\n'.format(nome, url))
				print('{} adicionado ao banco de dados'.format(nome))
		else:
			print('A url não é valida')

	
	def getURL(self, nome):
		try:
			return Sites.__sites_database[nome.encode()]
		except NameError:
			print('Site não pertence ao banco de dados')
			return None
		finally:
			pass

	def showDB(cls):
		for key in Sites.__sites_database.keys():
			print('{} URL:{}'.format(key, Sites.__sites_database[key]))

	@staticmethod
	def isSiteValid(url):
		DNS_valid = ('com', 'org', 'net', 'gov', 'eu', 'edu', 'br')
		s = tuple(url.split('.'))
		FLAG_isvalid = False
		
		if len(s) == 4 or len(s) == 3 and s[0] == 'www':
			if s[1].isalpha():
				if s[2] in DNS_valid:
					if len(s) == 3:
						FLAG_isvalid = True
					elif len(s) == 4:
						if s[3] == 'br':
							FLAG_isvalid = True

		return FLAG_isvalid



def interactUser(sites):
	print('DBM python v1.0 2020')
	print('--help para ajuda!\n')

	while True:
		print('>>', end=" ")

		opcao = input()

		if(opcao == 'quit'):
			break
		elif(opcao == 'help'):
			print('[find] -> Procurar o URL do site .: google')
			print('[add] -> Adicionar site com a respectiva URL .: google www.google.com')
			print('[show] -> Mostrar banco de dados completo')
			print('[quit] -> Sair do programa')
		elif(opcao == 'add'):
			nome, URL = str(input('>> ')).split()
			print('>>', end=" ")
			sites.addSite(nome, URL)
		elif(opcao == 'find'):
			nome = input('>> ')
			print('>> URL:{}'.format(sites.getURL(nome)))
		elif(opcao == 'show'):
			sites.showDB()
		else:
			print('>> Command not found')
			

		
def main():
	sites = Sites('sitesParaExemplo.txt')

	interactUser(sites)	

if __name__ == '__main__':
	main()
