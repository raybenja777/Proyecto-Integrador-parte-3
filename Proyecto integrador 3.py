
import os

def hacer_limpieza_de_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_un_numero(num):
    print(num)

def main():
    num = 0

    while num <= 50:
        hacer_limpieza_de_terminal()
        imprimir_un_numero(num)
        tecla = input('Presionar n:')

        if tecla.lower() == 'n':
            num += 1
        else:
            break

if __name__ == '__main__':
    main()