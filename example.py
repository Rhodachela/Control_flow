secret_guess = 17

guess_count = 0
guess = 0

while guess != secret_guess:
    guess_count +=1
    guess =int(input("Enter your guess: "))

print(f"You guessed it right in {guess_count}, tries!")

