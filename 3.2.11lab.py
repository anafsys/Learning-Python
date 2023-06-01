# Solicitar ao usuário que digite uma palavra

user_word = input("Enter a word: ")

# e atribua-o à variável user_word.
user_word = user_word.upper()

for word_without_vowels in user_word:
    # Completa o corpo do loop.
    if word_without_vowels == 'A':
        continue
    elif word_without_vowels == 'E':
        continue
    elif word_without_vowels == 'I':
        continue
    elif word_without_vowels == 'O':
        continue
    elif word_without_vowels == 'U':
        continue

# Imprima a palavra atribuída a word_without_vowels.
    print(word_without_vowels)
