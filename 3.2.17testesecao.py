''' Crie um loop for com contagem de 0 a 10 e imprima números ímpares na tela

for i in range(0,11):
    num = i % 2
    if num != 0: 
        print(i) '''

''' Pergunta 2: Crie um loop while que conta de 0 a 10 e imprime números ímpares na tela. 

x = 1
while x < 11:
    num = x % 2
    if num != 0:
        print(x)
    x += 1 '''

'''Crie um programa com um loop for e uma declaração de break. 
#O programa deve iterar os caracteres em um endereço de e-mail, 
#sair do loop quando atingir o símbolo @ e imprimir a peça antes de @ em uma 
#linha 

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="") '''

''' Pergunta 4: Crie um programa com um loop for e uma declaração continue. 
O programa deve repetir uma sequência de dígitos, substituir cada 0 por x e 
imprimir a sequência modificada na tela. 

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    else:
        print(digit, end="") '''