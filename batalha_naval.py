# -*- coding utf-8 -*-
import random

# Cria o Tabuleirp e suas matrizes
lista_aux = ['null', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']


def kant(tab):
    x = 1
    print("   A B C D E F G H I J K L M N O P Q R S")
    for i in tab:
        for j in range(len(i)):
            if x < 10:
                i[0] = '0' + str(x)
            else:
                i[0] = str(x)
            if i[j] == '~':
                i[j] = '~'
        print(" ".join(i))
        x += 1


tab1 = []
tab2 = []
for i in range(20):
    tab1.append(['~'] * 20)
    tab2.append(["~"] * 20)


def jogo(tab, char):
    for i in range(len(tab)):
        if char in tab[i]:
            return False
    return True


# Posicona os barcos para o robo
def leonboff(tab2, boats):
    one_direction = ['V', 'H']
    l = []
    for i in boats:
        while True:
            line = random.randint(1, 17)
            column = random.randint(1, 17)
            l.append(line)
            l.append(column)
            try:
                while line in l or column in l:
                    line = line = random.randint(1, 17)
                    column = random.randint(1, 17)
                x = cortella(random.choice(one_direction), line, column, i, tab2, imagem1)
                while x == False:
                    x = cortella(random.choice(one_direction), line, column, i, tab2, imagem1)
                    line = random.randint(1, 17)
                    column = random.randint(1, 17)
            except:
                pass
            else:
                break


# Bomba do Robo
def berkeley(tab1):
    line = random.randint(0, 19)
    column = random.randint(0, 19)
    x = bauman(line, column, tab1)


# Definições de variáveis

porta_aviao = 5
encouracado = 4
submarino = 3
destroyer = 3
barco = 2
boats = [porta_aviao, encouracado, submarino, destroyer, barco]
titulo = ['Porta Aviões', 'Encouraçado', 'Submarino', 'Destroyer', 'Barco']
imagem2 = chr(2017)
imagem1 = 'O'


# Função para posicionar os barcos e verificá-los
def cortella(direcao, l, c, tipo, tab, carac):
    lista = []
    x = 0
    if direcao == 'H':
        for i in range(tipo):
            lista.append(tab[l][c + i])
            for j in lista:
                if j != '~':
                    x += 1

        if x == 0:
            tab[l][c] = carac
            for i in range(tipo):
                tab[l][c + i] = carac


        else:
            while tab1[l][c] == imagem2:
                print("Este lugar já possui um barco")
                l = int(input("Digite uma linha válida:"))
                c = input("Digite uma coluna válida:").upper()
                c=lista_aux.index(c)
            tab[l-1][c] = carac
            for i in range(tipo):
                tab[l-1][c + i] = carac

    elif direcao == 'V':
        for i in range(tipo):
            lista.append(tab[l + i][c])
            for j in lista:
                if j != '~':
                    x += 1
        if x == 0:
            tab[l][c] = carac
            for i in range(tipo):
                tab[l + i][c] = carac
        else:
            while tab1[l][c] == imagem2:
                print("Este lugar já tem um barco!!")
                l = int(input("Digite uma linha válida:"))
                c = input("Digite uma coluna válida:").upper()
                c = lista_aux.index(c)
            tab[l-1][c] = carac
            for i in range(tipo):
                tab[l + i -1][c] = carac


# Função para explodir os barcos(artilharia pesada)
def bauman(linha, coluna, tabu):
    if tabu[linha][coluna] == '~':
        tabu[linha][coluna] = 'X'
        if tabu == tab2:
            print("Você Errou o Barco!")
        return False
    elif tabu[linha][coluna] == imagem1 or tabu[linha][coluna] == imagem2:
        tabu[linha][coluna] = "*"
        if tabu == tab2:
            print("Parabéns, você acertou o barco!!!")
        return True


# Inputs de posicionamento
print("POSICIONAMENTO DOS BARCOS")
contador = 0
for i in boats:
    kant(tab1)
    print('Posicione o %s de tamanho %dx1' % (titulo[contador], i))
    pitagoras = input("Em qual direção vc deseja jogar[V/H]:").upper()
    parmenides = int(input("Qual a linha que vc deseja jogar:"))
    platao = input("Qual a coluna que vc deseja jogar:").upper()
    platao = lista_aux.index(platao)
    cortella(pitagoras, parmenides - 1, platao, i, tab1, imagem2)
    contador += 1

leonboff(tab2, boats)


# Inputs para a Porrada:
cont = 0
print("ESTÁ NA HORA DE TACAR AS BOMBAS")
print("Os [X] que aparecem no seu tabuleiro querem dizer que o adversário errou a bomba")
print("Os [*] querem dizer que seu adversário acertou a bomba")

while not jogo(tab2, imagem1) or not jogo(tab1, imagem2):
    a = int(input("Em qual linha vc quer jogar:"))
    b = input("Em qual coluna vc quer jogar:").upper()
    b = lista_aux.index(b)
    bauman(a-1,b, tab2)
    berkeley(tab1)
    kant(tab1)
    if jogo(tab2, imagem1):
        print("VOCÊ GANHOU!!!!")
        kant(tab2)
        break
    if jogo(tab1, imagem2):
        print("VOCÊ PERDEU!")
        break
