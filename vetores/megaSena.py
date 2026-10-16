import random
import time
qntJogos = 0
i = 0


print("--" * 20)
print("NUMEROS DA MEGA SENA!")
print("--" * 20)


resposta = int(input("Quantos jogos você quer que eu sorteie? | "))
print("Carregando jogo(s)...")


while qntJogos < resposta:
    lista = random.sample(range(1, 101), 5)
    qntJogos = qntJogos + 1
    time.sleep(1.5)
    print(f'Jogo {i+1}: {lista}')
    i = i + 1
print("Jogo encerrado!!")
 

  
