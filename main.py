import sys
from gramatica import *

nombre_gramatica = "G"
start = Produccion("S", [".S","(S)","."],[0.6,0.1,0.3])
noTerminales = ["S"]

g = GLC(nombre_gramatica,start,noTerminales,produccionesIniciales = [])
derivador = Derivador()
palabra = derivador.derivar(g)
