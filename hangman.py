import random
words = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N')
while True:
    print('Type "play" to play the game, "exit" to quit:')
    action = input()
    if action == 'play':
        word = list(random.choice(words))
        hyphen_word = ['-'] * len(word)
        word_set = set(word)
        checked = set()
        number_of_attempts = 8
        attempt = 0
        hanged = True
        while attempt < number_of_attempts:
            print()
            print(''.join(hyphen_word))
            letter = input('Input a letter:')
            if len(letter) > 1:
                print('You should print a single letter')
                continue
            if not letter.islower():
                print('It is not an ASCII lowercase letter')
                continue
            if letter in word_set and letter not in checked:
                for i in range(len(word)):
                    if word[i] == letter:
                        hyphen_word[i] = letter
                checked.add(letter) 
            elif letter in checked:
                print('You already typed this letter')
            else:
                attempt += 1
                checked.add(letter) 
                print('No such letter in the word')
            if hyphen_word == word:
                print('You guessed the word!')
                print('You survived!')
                hanged = False
                break
        if hanged:
            print('You are hanged!')
    elif action == 'exit':
        break
