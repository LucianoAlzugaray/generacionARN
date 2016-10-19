import graphviz as gv

##############################################################################################

class Arbol:

	def __init__(self, nombreRaiz):
		self.arbol = gv.Graph(comment = "Arbol Generacion de ARN")
		self.arbol.node("0", nombreRaiz)
		
		self.hojas = []

		hoja = {'clave': 0, 'nombre': nombreRaiz}

		self.hojas.insert(0, hoja)
		styles = {
				'nodes': {
			        'fontname': 'Helvetica',
			        'shape': 'plaintext',
			        'color': 'white',
			        'style': 'filled',
			    }
			}

		self.arbol.node_attr.update(
		        ('nodes' in styles and styles['nodes']) or {}
		         )

		self.ultima_hoja = 0

##############################################################################################	

	def dibujarArbol(self, raiz, hojas_nuevas):
		indice = 0
		clave_hojaRaiz = '0'
		for hoja in self.hojas:
			if raiz == hoja['nombre']:
				clave_hojaRaiz = hoja['clave']
				indice = self.hojas.index(hoja)
				self.hojas.remove(hoja)
				break

		posicion = 0
		for hoja_nueva in hojas_nuevas:
			self.ultima_hoja = self.ultima_hoja + 1
			self.arbol.node(str(self.ultima_hoja), hoja_nueva)
			self.hojas.insert(indice + posicion, {'clave': self.ultima_hoja, 'nombre': hoja_nueva})
			self.arbol.edge(str(clave_hojaRaiz), str(self.ultima_hoja))
			posicion = posicion + 1
			print "ultima hoja: " + str(self.ultima_hoja) + " hoja nueva: " + hoja_nueva + " indice: " + str(indice) + " posicion: " + str(posicion) + " raiz: " + raiz + " clave raiz:" + str(clave_hojaRaiz)

##############################################################################################

	def crearImagen(self):
		ruta = './img/arbol'
		palabra = ''
		for hoja in self.hojas:
			palabra = palabra + hoja['nombre']
		print palabra
		self.arbol.render(ruta)
		