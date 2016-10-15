import sys

class GLC:
	def __init__(self, nombre):
		self.produciones = []

	def crearProduccion(self,noTerminal, producciones):
		p = Produccion(noTerminal,producciones)
		self.producciones.append(p)

	def mostrarGramatica(self):
		print self.nombre + ": {"
		for i in self.producciones:
			i.mostrarProduccion()
		print "}"

class Produccion:

	def __init__(self, noTerminal, producciones):
		if len(producciones) == 0 or noTerminal == "":
			raise ProduccionInvalida("Produccion Invalida")
		self.noTerminal = noTerminal
		self.producciones = producciones

	def mostrarProduccion(self):
		print self.noTerminal + " -> ",
		if len(self.producciones) > 1:
			lista = self.producciones[:len(self.producciones)-1]
			for i in lista:
				print i + " |",
		print self.producciones[len(self.producciones)-1]
