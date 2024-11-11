import random
print('Wellcome to the Guees the word game')
word_list = ['aardvark', 'babioon', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = " "
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
    print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guees = input('Guees a letter:').lower()


    display = ""

    for letter in chosen_word:
        if letter == guees:
            display += letter
            correct_letters.append(guees)
        else:
            display += "-"

    print(display)

    if "_" not in display:
        game_over = True
        print('you win') 
