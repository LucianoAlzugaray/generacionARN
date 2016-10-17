from gramatica import *
g = GLC("G", Produccion("S", [".S","(S)","."],[0.6,0.1,0.3]))
derivador = Derivador()
print derivador.derivar(g)

