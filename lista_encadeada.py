class Celula():
	def __init__(self, dado, proximo=None):
		self.__dado = dado
		self.__proximo = proximo

	def get_dado(self):
		return self.__dado

	def set_dado(self, object):
		self.__dado = object

	def get_proximo(self):
		return self.__proximo

	def set_proximo(self, proximo):
		self.__proximo = proximo

	dado = property(get_dado, set_dado)
	proximo = property(get_proximo, get_proximo)

class ListaEncadeada():
	def __init__(self, head=None, tail=None):
		self.__contador = 0
		self.__head = head
		self.__tail = tail

	def get_contador(self):
		return self.__contador

	def get_head(self):
		return self.__head

	def get_tail(self):
		return self.__tail

	def adiciona(self, dado):
		celula = Celula(dado)

		if self.__head == None:
			self.__head = celula
			self.__tail = celula
			self.__contador += 1
		else:
			# self.__head = celula
			self.__tail.set_proximo(celula)
			self.__tail = celula
			self.__contador += 1

	def remove():
		pass


	contador = property(get_contador)
	head = property(get_head)
	tail = property(get_tail)


listaEncadeada = ListaEncadeada()
listaEncadeada.adiciona('teste1')
print(listaEncadeada.head.proximo)
listaEncadeada.adiciona('teste2')
print(listaEncadeada.head.proximo)
listaEncadeada.adiciona('teste3')
print(listaEncadeada.head.proximo)

print(listaEncadeada.contador)