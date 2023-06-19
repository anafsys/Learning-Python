
'''Etapa 1: escreva uma linha de código que solicita ao usuário que substitua o número do meio por um 
número inteiro inserido pelo usuário''' 

hat_list = [1, 2, 3, 4, 5] # Esta é uma lista atual de números ocultos no hat.

new_num = int(input("Choose a new middle number: "))

hat_list[2] = new_num

# Etapa 2: escreva uma linha de código que remova o último elemento da lista.

del hat_list[4]

# Etapa 3: escreva uma linha de código que imprima o comprimento da lista atual

print (len(hat_list))
print (hat_list) 