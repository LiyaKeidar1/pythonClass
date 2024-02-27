import random

def computer_guess(x:int):
    low = 1
    high = x
    feedback = ''
    try:
        while feedback != "c":
            guess = random.randint(low,high)
            feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?").lower()
            if feedback == "h":
                high = guess - 1
            elif feedback == "l":
                low = guess + 1
    except ValueError:
        print("no more options you liar")
    print("computer guessed correctly")

computer_guess(100)