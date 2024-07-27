from objetos.Forma import Forma
from objetos.Circulo import Circulo
from objetos.Retangulo import Retangulo
import os

def exibir_menu():
    os.system('clear')
    print('***********************')
    print('*** Calculo de Area ***')
    print('***********************')
    print('1. Para area do retangulo')
    print('2. Para area do circulo')
    print('3. Para sair')

def escolher_opcao():
    opcao_escolhida = int(input('Opcao: '))

    match opcao_escolhida:
        case 1:
            os.system('clear')
            base: float = float(input('Digite a base do retangulo: '))
            altura: float = float(input('Digit a altura do retangulo: '))
            retangulo: object = Retangulo(base, altura)
            retangulo.calcular_area()
            input('----- Digite qualquer tecla para voltar ao menu principal: ')
            main()
        case 2:
            os.system('clear')
            raio: float = float(input('Digite o valor do raio do circulo: '))
            circulo: object = Circulo(raio)
            circulo.calcular_area()
            input('----- Digite qualquer tecla para voltar ao menu principal: ')
            main()
        case 3:
            print()
            print('Obrigado!\n')
        case _:
            print('Opcao inválida! Tente novamente.')
            input('----- Digite qualquer tecla para voltar ao menu principal: ')
            main()

def main():
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()