from random import randint

answer = randint(1, 100)
for i in range(6):
    guess = int(input('guess: '))
    if guess > answer:
        print("Down")
    elif guess < answer:
        print("Up")
    else:
        print("Victory")
        exit(1)

print("Gameover")
print("Answer is: ", answer)
