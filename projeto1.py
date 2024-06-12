'''
Crie um programa que recebe um número e imprime o fatorial daquele número
#Método 5Qs para montar o algoritmo
1. Quais os dados de entrata necessários?
numero
2. O que devo fazer com estes dados?
calcular o fatorial do número que for passado para o programa e exibir na tela
3. Quais são as restrições deste problema?
- O número deve ser um valor positivo
_ O número deve ser um valor inteiro
4. Qual é o resultado esperado?
 Que o fatorial do numero providenciado seja exibido.
5. Qual é a sequência de passos a ser feitas para chegar ao resultado esperado?
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
fatorial *= numero
print fatorial
'''
numero = int(input('Digite um número: '))
if numero > 0:
  fatorial = 1
  for item in range(1, numero + 1):
    fatorial *= item
  print(fatorial)