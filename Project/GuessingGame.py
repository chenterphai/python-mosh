secret_number = 9
i = 0
j = 3
while i < j:
    guess = int(input("Guess: "))
    i += 1
    if guess == secret_number:
        print("Congratulations! You Win")
        break
    else:
        print("Sorry, you missed!")
