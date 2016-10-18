import sys
import numpy as np
import controlador

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
		if eval('+'.join(probabilidades) == 1.0 and len(probabilidades) == len(producciones)):
			self.probabilidades = probabilidades
		else:
			raise ProduccionException("Las probabilidades tienen un error de definicion")
			
##############################################################################################

class Derivador:

	def derivar(self,gramatica):
		controlador = Controlador()
		arbol = controlador.inicializarArbol(gramatica.start.noTerminal,)
		palabra = self.derivarPalabra(gramatica, gramatica.start, gramatica.start.noTerminal, arbol)
		arbol.render('img/' + palabra)
		return palabra

	def derivarPalabra(self,gramatica, derivacion, palabra, arbol):
		derivado = np.random.choice(derivacion.producciones, None, None, derivacion.probabilidades)
		controlador.dibujarArbol(arbol,raiz)
		palabra = palabra.replace(derivacion.noTerminal, derivado)
		for caracter in palabra:
			if caracter in gramatica.noTerminales:
				seEncontro = False
				for i in gramatica.producciones:
					if caracter == i.noTerminal:
						seEncontro = True
						palabra = self.derivarPalabra(gramatica, i, palabra)
				if not seEncontro:
					raise DerivacionException("Un no terminal no tiene derivacion explicita")
		return palabra							
