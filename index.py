'''
carro1 = {
    "marca": "Fiat",
    "modelo": "Uno",
    "ano": "2025" 
}

print(carro1)
'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

uno = Carro("Fiat", "Uno", "2001")
gol = Carro("Volkswagen", "Fiat", "2012")

print(uno.ano)
print(gol.marca)