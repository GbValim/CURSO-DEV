# Desenvolva um programa que solicite dois números
#  inteiros representando os


# limites de um intervalo [A, B]
#  (garantindo que A ≤ B).
#  O programa deve iterar sobre
# o intervalo utilizando uma estrutura de repetição
#  e calcular a soma apenas dos
# números ímpares presentes nele,
#  exibindo o resultado final ao usuário.

resultado = []
soma = 0
# Desenvolva um programa que solicite dois números
numeroUm = int(input("Digite seu primeiro numero"))
numeroDois = int(input("Digite seu segundo numero"))

while (numeroDois <= numeroUm):
  numeroUm = int(input("Digite seu primeiro numero"))

# Iteração
for i in range (numeroUm, numeroDois+1):
   
 resultado.append(i)
for j in range(len(resultado)): 
       # print(resultado[j])
        if (resultado[j] % 2 != 0):
            soma += resultado[j]
print(soma)


          






     




    


