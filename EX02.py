class Quadrado :
    def __init__(self, lado, area) :
        self.lado = lado
        self.area = area
    def vlado(self):
        return self.lado
if __name__ == "__main__" :
    lado =float( input("informe os lados do quadrado :"))
    area = print(f"area do quadrado é {lado*lado}")
    quadrado = Quadrado(lado=lado,area=area)
    print("lado do quadrado", quadrado.vlado())


    

    