class retangulo :
    def __init__(self, ladoA, ladoB,area, perimetro) :
        self.lado = ladoA
        self.lado = ladoB
        self.area = area
        self.perimetro = perimetro

    def vladoA(self):
        return self.ladoA
    
    def vladoB(self):
        return self.ladoB
if __name__ == "__main__" :
        ladoA = float(input("informe o lado :"))
        ladoB = float(input("informe o lado :"))
        area = print(f"area do retangulo é igual a {ladoA * ladoB}")
        perimetro = print(f"area do triangulo é igual a {(ladoA * ladoB)*2}")
        retangulo = retangulo(ladoA = ladoA, ladoB = ladoB)
print("base do retangulo :", retangulo.vladoA())
print("altura do retangulo :", retangulo.vladoB())

    

