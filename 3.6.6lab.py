my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
exclusive = []
for number in my_list:
  if number not in exclusive:
    exclusive.append(number)

print("A lista com os elementos exclusivos aqui")
print(exclusive)
#