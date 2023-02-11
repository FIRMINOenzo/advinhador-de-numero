from random import randint
from time import sleep
import re


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True


print("-"*30)
print(f"{'ADIVINHE O NÚMERO!':^30}")
print('-'*30)

print(f"{'MENU':^30}")
print("1 - JOGADOR TENTAR ADVINHAR")
print("2 - MÁQUINA TENTAR ADVINHAR")

while True:
    escolha = str(input("Digite sua escolha: "))

    if escolha == '1':
        while True:
            numLimite = str(input("Digite o número limite a ser gerado: "))

            if(is_int(numLimite)):
                numLimite = int(numLimite)
                break

            else:
                print("Digite apenas números inteiros.")
                sleep(1)

        numGerado = randint(0, numLimite)
        tentativas = 0

        while True:
            while True:
                numTentativa = str(input("Digite um número: "))

                if(is_int(numTentativa)):
                    numTentativa = int(numTentativa)
                    break

                else:
                    print("Digite apenas números inteiros.")
                    sleep(1)
            
            if numTentativa == numGerado:
                tentativas += 1
                print("Você acertou o número gerado!")
                print(f"Tentativas: {tentativas}")
                sleep(1)
                break
            
            elif numTentativa > numGerado:
                tentativas += 1
                print("Tente digitar um número menor...")
                sleep(1)
            
            else:
                tentativas += 1
                print("Tente digitar um número maior...")
                sleep(1)
        break

    elif escolha == '2':
        while True:
            numLimite = str(input("Digite o número limite a ser gerado: "))

            if(is_int(numLimite)):
                numLimite = int(numLimite)
                break

            else:
                print("Digite apenas números inteiros.")
                sleep(1)

        numGerado = randint(0, numLimite)
        numMin = 0
        numMax = numLimite
        tentativas = 0

        while True:
            numTentativa = randint(numMin, numMax)

            if numTentativa == numGerado:
                tentativas += 1
                print("A máquina acertou o número gerado!")
                print(f"O número era: {numGerado}")
                print(f"Tentativas: {tentativas}")
                sleep(1)
                break
            
            elif numTentativa > numGerado:
                tentativas += 1
                print(f'Tentativa da máquina: {numTentativa} - Valor alto')
                numMax = numTentativa - 1
                print(numMin, numMax)
                sleep(1)
            
            else:
                tentativas += 1
                print(f'Tentativa da máquina: {numTentativa} - Valor baixo')
                numMin = numTentativa + 1
                print(numMin, numMax)
                sleep(1)
        break

    else:
        print("Você não escolheu algo do menu, tente novamente.")