import sys
from gramatica import *

nombre_gramatica = "G"
start = Produccion("S", ["SS","(S)","."],[0.35,0.35,0.3])
noTerminales = ["S"]

g = GLC(nombre_gramatica,start,noTerminales,produccionesIniciales = [])
derivador = Derivador()
palabra = derivador.derivar(g)

print palabra