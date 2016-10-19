import sys
from subprocess import call 
from gramatica import *

nombre_gramatica = "G"
start = Produccion("S", ["SS","(S)","."],[0.35,0.35,0.3])
noTerminales = ["S"]

call(["rmdir", "img"])
g = GLC(nombre_gramatica,start,noTerminales,produccionesIniciales = [])
derivador = Derivador()
palabra = derivador.derivar(g)

print palabra