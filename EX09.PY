class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self): 
        if self.largura %2 == 1 and self.altura %2 == 1:
            larguraCentro = (self.largura /2) + 0.5
            alturaCentro = (self.altura /2) + 0.5
            print(f'\nO centro do retangulo está na posição:\nLargura: {larguraCentro:.0f}\nAltura: {alturaCentro:.0f}')
        else:
            print(f'\Impossivel achar o centro pois os valores não são impares')
    
class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimirPonto(self):
        if self.x == 0 or self.y == 0:
            p = Ponto.pontoPartida(self)
            print(f'\nO ponto está na posição inicial:\nLargura: {p[0]}\nAltura: {p[1]}')
        else:
            print(f'\nO ponto está na posição:\nLargura: {self.x}\nAltura: {self.y}')
  
    def pontoPartida(self):
        larguraInicial = 2
        alturaInicial = self.y - 1
        print(f'\nO ponto está na posição inicial:\nLargura: {larguraInicial}\nAltura: {alturaInicial}')
        inicioPonto = [larguraInicial, alturaInicial]
        return inicioPonto  
    
quad1 = Retangulo(7,5)
quad1.encontrarCentro()

quad1 = Ponto(5,6)
quad1.imprimirPonto()
quad1.pontoPartida()