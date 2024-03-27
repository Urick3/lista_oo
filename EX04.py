class Pessoa() :
    def __init__(self, nome,idade,peso,altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos) :
        self.idade += anos
        if self.idade < 22 :
            self.altura += 0.5 * anos
    def engordar(self, peso):
        self.peso += peso

    def emagrecer (self, peso) :
        self.peso -= peso

    def crescer (self, altura) :
        self.altura += altura

pessoa1 = Pessoa("Carla", 19,70,160)
print("altura antes de envlehecer", pessoa1.altura)
pessoa1.envelhecer(2)
print("altura depois de envelhecer",pessoa1.altura)




