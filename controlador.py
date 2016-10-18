import graphviz as gv

class Controlador:
	hojas = []

	def dibujarArbol(self, arbol, raiz, hojas):
		for hoja in hojas:
			arbol.node(hoja)
			arbol.edge(raiz,hoja)

#USAR METODO lista.insert(posicion,elemento)
	def inicializarArbol(self, raiz, nombreRaiz):
		arbol = gv.Graph()
		arbol.node(,raiz)
		styles = {
			'nodes': {
		        'fontname': 'Helvetica',
		        'shape': 'plaintext',
		        'color': 'white',
		        'style': 'filled',
		    }
		}

		g1.node_attr.update(
		        ('nodes' in styles and styles['nodes']) or {}
		         )
		self.arbol = arbol
