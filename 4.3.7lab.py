def is_prime(num):
 #
 # if num => 1:
  return True
 elif num % 2 == 0:
  return False
 elif num % 3 == 0:
  return False
 elif num % 5 == 0:
  return False
 
 
 elif year % 400 != 0:
  return False
 else:
  return True
 #

 for i in range(1, 20):
  if is_prime(i + 1):
   print(i + 1, end=" ")
print()

''' 
Para saber se um número é primo, dividimos esse número pelos números primos 2, 3, 5, 7, 11, 
etc, até que tenhamos:
- ou uma divisão com resto zero (e neste caso o número não é primo),
- ou uma divisão com quociente menor que o divisor e o resto diferente de zero. 
Neste caso o número é primo.

Um número natural é primo se for maior que 1 e não tiver divisores diferentes de 1 e 
ele próprio.
Complicado? Não mesmo. Por exemplo, 8 não é um número primo, pois você pode dividi-lo por 2 e 4
(não podemos usar divisores iguais a 1 e 8, pois a definição proíbe isso).
Por outro lado, 7 é um número primo, pois não podemos encontrar divisores legais para ele.
Sua tarefa é escrever uma função verificando se um número é primo ou não.

A função:

é chamado is_prime;
requer um argumento (o valor a ser verificado)
retorna True se o argumento for um número primo e False caso contrário.
Dica: tente dividir o argumento por todos os valores subsequentes (começando em 2) e verifique 
o restante - se for zero, seu número não pode ser um primo; pense bem quando deve 
interromper o processo.

Se você precisar conhecer a raiz quadrada de qualquer valor, poderá utilizar o operador **. 
Lembre-se: a raiz quadrada de x é o mesmo que x0.5

Preencha o código no editor.
Execute o código e verifique se a saída é igual à nossa.

Saída prevista:

2 3 5 7 11 13 17 19'''