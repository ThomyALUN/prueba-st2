class HashTable:
    diccCol={
            0:"listaEnlz",
            1:"saltoUnit",
            2:"saltoFijo",
            3:"saltoCuad"
            }
    def __init__(self, longitud:int, tipoCol:int):
        self.tamanio=longitud
        self.tabla=[None]*longitud
        self.colision=self.diccCol[tipoCol]
        self.numCol=0

    def calcularHash(self, valor):
        ind=valor%self.tamanio
        return ind

    def ingresarDatos(self, valor):
        ind=self.calcularHash(valor)
        if self.tabla[ind]==None:
            self.tabla[ind]=valor
        else:
            self.numCol+=1
            self.paso(valor, ind)

    def paso(self, valor, ind:int, paso:int=1):
        posPosibles=[i for i in range(self.tamanio)]
        pos=ind
        while True:
            if len(posPosibles)==0:
                break
            elif pos in posPosibles and self.tabla[pos]==None:
                self.tabla[pos]=valor
                break
            else:
                try:
                    posPosibles.remove(pos)
                except ValueError:
                    pass
                else:
                    pos+=paso

    def getTabla(self):
        return self.tabla
    
    def getOcupacion(self):
        return (self.tamanio - self.tabla.count(None))/self.tamanio
    
    def getColisiones(self):
        return self.numCol
    
    def getTamanio(self):
        return self.tamanio
    
    def __str__(self) -> str:
        datos="La tabla hash cuenta con los siguientes atributos:"
        datos+=f"\nTamaño: {self.getTamanio()}"
        datos+=f"\nOcupación: {self.getOcupacion()*100:.2f}%"
        datos+=f"\nColisiones: {self.getColisiones()}"
        return datos
