import random
from time import sleep

senha = []

Int = '0123456789'
char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(0,4):
    senha.append(random.choice(Int))

for c in range(0,4):
    senha.append(random.choice(char))

senha = ''.join(random.sample(senha, len(senha)))

sleep(.5)

print('-'*10,f'\033[32m{senha}\033[0m','-'*10)

# Gerador de senhas com 4 números e 4 letras
# O código gera uma senha aleatória composta por 4 números e 4 letras, misturando-as.
# A senha é exibida na tela com uma pausa de 0,5 segundos antes da exibição.
# O código utiliza as bibliotecas random e time para gerar a senha e controlar o tempo de exibição.