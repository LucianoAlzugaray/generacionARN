import sys
import numpy as np
import arbol as tree

###########################################################################################e
class GLC:

	def __init__(self, nombre, start, alfabetoNoTerminales, produccionesIniciales = []):
		self.producciones = produccionesIniciales
		self.nombre = nombre
		self.start = start
		self.producciones.append(start)
		self.noTerminales = alfabetoNoTerminales

	def agregarProduccion(self,noTerminal, producciones, probabilidades):
		p = Produccion(noTerminal,producciones, probabilidades)
		self.producciones.append(p)

	def mostrarGramatica(self):
		print self.nombre + ": {"
		for i in self.producciones:
			i.mostrarProduccion()
		print "}"

##############################################################################################

class Produccion:
	def __init__(self, noTerminal, producciones, probabilidades):
		if len(producciones) == len(probabilidades):
			self.noTerminal = noTerminal
			self.producciones = producciones
			self.probabilidades = probabilidades
		else:
			raise ProductionException("Las probabilidades tienen un error de definicion")

	def mostrarProduccion(self):
		print self.noTerminal + " -> ",
		if len(self.producciones) > 1:

			lista = self.producciones[:len(self.producciones)-1]
			for i in lista:
				print i + " |",
		print self.producciones[len(self.producciones)-1]

	def cambiarProbabilidades(self, probabilidades):
		if len(probabilidades) == len(self.producciones):
			self.probabilidades = probabilidades
		else:
			raise ProduccionException("Las probabilidades tienen un error de definicion")
			
##############################################################################################

class Derivador:

	def derivar(self,gramatica):
		arbol = tree.Arbol(gramatica.start.noTerminal)
		palabra = self.derivarPalabra(gramatica, gramatica.start, gramatica.start.noTerminal, arbol)
		arbol.crearImagen(palabra)
		return palabra

	def derivarPalabra(self, gramatica, derivacion, palabra, arbol):
		derivado = np.random.choice(derivacion.producciones, None, None, derivacion.probabilidades)
		print derivado
		arbol.dibujarArbol(derivacion.noTerminal, derivado)
		palabra = palabra.replace(derivacion.noTerminal, derivado)
		for caracter in palabra:
			if caracter in gramatica.noTerminales:
				seEncontro = False
				for i in gramatica.producciones:
					if caracter == i.noTerminal:
						seEncontro = True
						palabra = self.derivarPalabra(gramatica, i, palabra, arbol)
						break
				if not seEncontro:
					raise DerivacionException("Un no terminal no tiene derivacion explicita")
				break
		return palabra							

	def derivarPalabra(self, gramatica, derivacion, palabra, arbol):
		derivado = np.random.choice(derivacion.producciones, None, None, derivacion.probabilidades)
		terminal = True
		for caracter in derivado:
			if caracter in gramatica.noTerminales:
				terminal = False

		arbol.dibujarArbol(derivacion.noTerminal, derivado)

		if terminal:
			return palabra.replace(derivacion.noTerminal, derivado)
		else:
			for caracter in derivado:
				if caracter in gramatica.noTerminales:
					seEncontro = False
					for i in gramatica.producciones:
						if caracter == i.noTerminal:
							seEncontro = True
							palabra = palabra.replace(caracter, self.derivarPalabra(gramatica, i, caracter, arbol))
							break
					if not seEncontro:
						raise DerivacionException("Un no terminal no tiene derivacion explicita")
		
			return palabra							
