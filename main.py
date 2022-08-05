import platform
from os import system
from pessoa import Pessoa
from paises import Moedas
from conversor import ConversorMoedas

def clear():
    if platform.system() == 'Windows':
        system('cls')
    else: 
        system('clear')

clear()

nome = str(input('Digite o seu nome: '))
pais_pessoa = str(input('Digite o seu pais: '))
pessoa = Pessoa(nome , pais_pessoa)
input('Pressione qualquer tecla para continuar')

clear()

print(pessoa)

print('\nEscolhendo a primeira moeda')
moeda1 = Moedas().escolher()
print(moeda1)
input('Pressione qualquer tecla para continuar')

clear()

print('Escolhendo a segunda moeda')
moeda2 = Moedas().escolher()
print(moeda2)
input('Pressione qualquer tecla para continuar')

clear()

conversor = ConversorMoedas(moeda1['moeda'], moeda2['moeda'])

print(f'Converter de {moeda1["pais"]}-${moeda1["moeda"]} para {moeda2["pais"]}-${moeda2["moeda"]}')
print(f'Cotação atual: {conversor.cotacao_atual()}')

valor = float(input('\n\nValor para converter: '))
print(f'${conversor.converter(valor):.2f}')