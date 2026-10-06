# Construa um programa que leia 10 números inteiros, armazene-os em uma lista e,
# em seguida, solicite um número adicional para consulta. O sistema deve verificar e
# exibir se esse valor está presente no vetor e a quantidade exata de vezes que ele se
# repete.
lista = []
contador = 0
for i in range (0, 10):
   lista.append(int(input(f'Digite o {i+1}° numero')))

ververificacao = int(input(f'Digite um numero para verificação'))

for j in range (0, 10):
   if ververificacao == lista[j]:
      contador +=1
if contador > 0:
   print(f"O numero adicionado já está na lista. Foi inserido {contador} vezes")
      


    