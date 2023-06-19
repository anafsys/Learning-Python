# etapa 1 criar uma lista vazia chamada beatles;

beatles = []
print("Etapa 1:", beatles)

# etapa 2 use o método append() para adicionar os seguintes membros da banda 
# à lista: John Lennon, Paul McCartney e George Harrison;

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Etapa 2:", beatles)

# etapa 3 Use o loop for e o método append() para solicitar que o usuário 
# adicione os seguintes membros da banda à lista: Stu Sutcliffe e Pete Best;

for member in range(2):
    beatleName = input("New Beatle name? ")
    beatles.append(beatleName)  
print ("Etapa 3:", beatles)

# etapa 4 use a instrução del para remover Stu Sutcliffe e Pete Best da lista;
del beatles[3:5]
print("Etapa 4:", beatles)

# passo 5 Use o método insert() para adicionar Ringo Starr ao início da lista.

beatles.insert(0,"Ringo Star")
print("Etapa 5:", beatles)

# testando o tamanho da lista

print("the fabulous", len(beatles))

