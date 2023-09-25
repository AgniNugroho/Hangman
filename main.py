import random
import os

country = ['indonesia', 'malaysia', 'laos', 'vietnam', 'cambodia', 'brunei', 'thailand', 'philippines', 'singapore', 'myanmar']
chance = 5

word = random.choice(country)
answer = []

for space in word:
    answer += '_'

while chance > 0:
    os.system('cls')
    print(answer)
    print(f'Sisa {chance} kesempatan')
    inp = input('> ')
    inp.lower()

    for pos in range(len(word)):
        letter = word[pos]
        
        if letter == inp:
            answer[pos] = letter

    if inp not in answer:
        chance -= 1
    
    if '_' not in answer:
        os.system('cls')
        print(answer)
        print('You Win')
        break

    elif inp == word:
        os.system('cls')
        answer.clear()
        for pos in range(len(word)):
            answer.append(word[pos])
        print(answer)
        print('You Win')
        break
    
    elif chance == 0:
        print('You Lose')
        break
    