import random as rnd
number = rnd.randint(1,100)
print("HOW2PLAY: Enter between 1-100 (integer)numbers. \
You have 5 chance! GOOD LUCK :)".center(100,"-"))
hp = 5
print(number)
while True:
    try:
        guess = int(input("Enter your guess: "))
        check_int = isinstance(guess,int)
        if check_int:
            if guess <= 0:
                print("Number must above 0")
            else:
                if hp != 1:    
                    if guess < number:
                        hp -= 1
                        print(f"UP hp:{hp}")
                    elif guess > number:
                        hp -= 1
                        print(f"DOWN hp:{hp}")
                    else:
                        print("Congrats you win!")
                        break
                else:
                    print(f"Chance over. The number was {number}")
                    break
        else: 
            raise ValueError
    except ValueError:
        print(f"You must enter a INTEGER NUMBER,not enter a text or decimal . ")