import sys
from subprocess import call 
from gramatica import *

nombre_gramatica = "G"
try:
	if sys.argv[1] == "-ps":
		start = Produccion("S", 
		["SS","(S)","."],
		[0.35,0.35,0.3])

	elif sys.argv[1] == "-ss":
		start = Produccion("S", 
		["SS","cSg","gSc", "uSa", "aSu", "aSa", "gSu", "g", "u", "a", "c"],
		[0.35, 0.05,0.05,0.05,0.05, 0.025,0.025,0.1,0.1,0.1,0.1])
except Exception:
	print "Modo de uso:  main.py [opcion]"
	print "Opciones: "
	print "-ps : Muestra estructura primaria "
	print "-ss : Muestra estructura secundaria "
	exit()

noTerminales = ["S"]

g = GLC(nombre_gramatica,start,noTerminales,produccionesIniciales = [])
derivador = Derivador()
derivador.derivar(g)
