blocos = int(input("Insira o número de blocos:"))  
 # Escreva seu código aqui.
altura = 0
blocos_usad = 0
camada = 1

while blocos_usad < blocos:
    blocos_usad += camada
    if blocos_usad > blocos:
        break
    else:
        altura += 1
        camada += 1
    
print("A altura da pirâmide:", altura)