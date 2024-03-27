class bola :
    def __init__(self, cor, circunferencia, material) :
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

def trocar_cor(self, n_cor) :
    self.cor = n_cor
def mostrar_cor(self) :
    return self.cor

if __name__ == "__main__" :
    cor = input("insira a cor da bola: ")
    circunferencia = float (input("digite a circunferencia da bola :"))
    material = input("digite o material da bola :")
    bola = bola(cor = cor, circunferencia = circunferencia, material = material)
    print("cor da bola :", bola.mostrar_cor())
    n_cor = input("nova cor da bola :")
    bola.trocar_cor(n_cor)
    print("nova cor da bola", bola.mostrar_cor())