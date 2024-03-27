class bombaCombustivel :
    def __init__(self, tipo_combustivel:str,valor_litro:float,quantidade:float) :
        self .__tipo_combustivel = tipo_combustivel
        self .__valor_litro = valor_litro
        self .__quantidade = quantidade 
    @property
    def tipo_combustivel(self) :
        return self .__tipo_combustivel
    @property
    def valor_litro(self) :
        return self .__valor_litro
    @property
    def quantidade(self) :
        return self .__quantidade
    
    def abastecer_valor(self,valor) :
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade :
            self.__quantidade -= litros_abastecidos
            return f"foram abastecidos{litros_abastecidos}"
        
    def abastecer_litro(self,litro_abastecer):
        self .__quantidade -= litro_abastecer
        return self .__valor_litro * litro_abastecer
    
    def alterar_valor (self, novo_valor) :
        self .__valor_litro = novo_valor

    def alterar_combustivel (self, novo_combustivel) :
        self .__tipo_combustivel = novo_combustivel
        return self.tipo_combustivel
    
    def alterar_quantidade(self,nova_quantidade):
        self.__quantidade = nova_quantidade
bomba_gasolina = bombaCombustivel("Gasolina", 5.50,100)
print(bomba_gasolina.abastecer_valor(55))
print(bomba_gasolina.abastecer_litro(20))
print(bomba_gasolina.alterar_valor(5.70))
print(bomba_gasolina.alterar_combustivel("etanol"))
print(bomba_gasolina.alterar_quantidade(150))