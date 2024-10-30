import os
import random
from colorama import Fore

jogarNovamente = "s"
jogada = 0
quemJoga = 2
maxJogadas = 9
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global velha
    global jogada
    os.system("cls" if os.name == "nt" else "clear")  
    print("    0  1  2")
    for i in range(3):
        print(f"{i}:  " + " | ".join(velha[i]))
        if i < 2:
            print("   -----------")
    print("Jogadas: " + Fore.BLUE + str(jogada) + Fore.RESET)

def jogadorJoga():
    global jogada
    global quemJoga
    while quemJoga == 2 and jogada < maxJogadas:
        try:
            l = int(input("Linha (0-2): "))
            c = int(input("Coluna (0-2): "))
            if velha[l][c] != " ":
                print("Posição já ocupada. Tente novamente.")
            else:
                velha[l][c] = "X"
                quemJoga = 1
                jogada += 1
        except (ValueError, IndexError):
            print("Jogada inválida. Tente novamente.")
            os.system("pause")

def cpuJoga():
    global jogada
    global quemJoga
    while quemJoga == 1 and jogada < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        if velha[l][c] == " ":
            velha[l][c] = "O"
            jogada += 1
            quemJoga = 2

def verificaVencedor():
    for i in range(3):
        if velha[i][0] == velha[i][1] == velha[i][2] != " ":
            return velha[i][0]
        if velha[0][i] == velha[1][i] == velha[2][i] != " ":
            return velha[0][i]
    if velha[0][0] == velha[1][1] == velha[2][2] != " ":
        return velha[0][0]
    if velha[0][2] == velha[1][1] == velha[2][0] != " ":
        return velha[0][2]
    return None


while jogarNovamente.lower() == "s":
    jogada = 0
    quemJoga = 2
    velha = [[" ", " ", " "] for _ in range(3)]

    while jogada < maxJogadas:
        tela()
        if quemJoga == 2:
            jogadorJoga()
        else:
            cpuJoga()

        vencedor = verificaVencedor()
        if vencedor:
            tela()
            print(f"{Fore.GREEN}Jogador {vencedor} venceu!{Fore.RESET}")
            break
    else:
        tela()
        print(f"{Fore.YELLOW}Empate!{Fore.RESET}")

    jogarNovamente = input("Deseja jogar novamente? (s/n): ")
