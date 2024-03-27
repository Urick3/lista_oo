class BichinhoVirtual:
    def __init__(self, nome, fome=0, saude=100, idade=0):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def fome(self):
        return self._fome

    @fome.setter
    def fome(self, valor_fome):
        if 0 <= valor_fome <= 100:
            self._fome = valor_fome
        else:
            print("Valor de fome deve estar entre 0 e 100.")

    @property
    def saude(self):
        return self._saude

    @saude.setter
    def saude(self, valor_saude):
        if 0 <= valor_saude <= 100:
            self._saude = valor_saude
        else:
            print("Valor de saúde deve estar entre 0 e 100.")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            print("Idade deve ser um valor positivo.")

    @property
    def humor(self):
        return (self._fome + self._saude) / 2

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, valor_fome):
        self.fome = valor_fome

    def alterar_saude(self, valor_saude):
        self.saude = valor_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

bichinho = BichinhoVirtual("Tamagushi")
print(bichinho.retornar_nome()) 
print(bichinho.retornar_fome()) 
print(bichinho.retornar_saude())  
print(bichinho.retornar_idade())  
print(bichinho.humor)  

bichinho.alterar_fome(50)
bichinho.alterar_saude(80)
print(bichinho.humor) 

bichinho.alterar_idade(1)
print(bichinho.retornar_idade()) 