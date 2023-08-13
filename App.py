import random as rnd
import math

def Game():
    number = rnd.randint(0, 99)
    question_left = 5
    guess = 3

    print("How to play?")
    print("* We'll random number between 0 -> 99")
    print("* You can gather information about number through command, but you're limit to asking only 5 question")
    print("* You'll be able to get a list of command by using \"cmd\" command P.S. Using \"cmd\" command not count as asking question")
    print("* To answer, you'll need to use \"Answer\" followed by your guess")
    print("* You get only 3 guesses. If you used all your guesses and still not won yet, you'll lose")

    while True:
        cmd = input("Please Enter your command : ")
        if len(cmd) == 0:
            print("Your previous command is empty please enter something")
            continue

        match cmd.split()[0].lower():
            case 'answer' | 'ans':
                if len(cmd.split()) < 2:
                    print("Look like you only have \"Answer\", but not the guessed number. Please re enter")
                    continue

                answer = cmd.split()[1]
                
                try:
                    answer = int(answer)

                    if answer == number:
                        print(f"Congratulation! You won {question_left} points")

                        return question_left
                    else:
                        guess -= 1

                        if guess <= 0:
                            print("Wrong, you got no guesse left. You lose!")

                        print(f"Wrong, you got {guess} guesses left")
                        print(f"The Number is a {'bit' if abs(answer - number) <= 15 else 'lot'} {'higher' if number - answer > 1 else 'lower'}")
                except:
                    print("Look like your guessed is not a number. Please re enter")

            case 'cmd':
                print("List of Commands")
                print("* answer [guessed] => use to answer when you're ready, you only got 3 guesses per game")
                print("* cmd => use to see the list of commands")
                print("* oddeven => use to tell if number is odd or even")
                print("* prime => use to tell if number is prime number")
                print("* sqrt => use to tell if number if perfect square")
                print("* compare [numberX] => use to tell if number is higher or lower than numberX")
                print("* multiple [factor] => use to tell if number is multiple of factor number")
                print("* factor [numberX] => use to tell if number is factor of numberX")

            case 'oddeven' | 'odd' | 'even':
                if question_left <= 0:
                    print("You have no question left")
                    continue
                question_left -= 1 
                print(f"Number is {'Odd' if number % 2 != 0 else 'Even'}")
                print(f"You have {question_left} Lefts")

            case 'prime':
                if question_left <= 0:
                    print("You have no question left")
                    continue
                question_left -= 1
                
                if number in [0, 1]:
                    print("Number is not prime number")

                for n in range(2, number):
                    if number % n == 0:
                        print("Number is not prime number")
                        break
                    elif number - 1 == n:
                        print("Number is prime number")

                print(f"You have {question_left} Lefts")

            case 'sqrt':
                if question_left <= 0:
                    print("You have no question left")
                    continue
                question_left -= 1

                print(f"Number is {'not ' if math.sqrt(number) % 1 != 0 else ''}perfect square")

                print(f"You have {question_left} Lefts")
            
            case 'compare':
                if question_left <= 0:
                    print("You have no question left")
                    continue

                if len(cmd.split()) < 2:
                    print("Look like you only have \"compare\", but not the reference number. Please re enter")
                    continue

                reference = cmd.split()[1]
                
                try:
                    reference = int(reference)

                    question_left -= 1
                    if reference == number:
                        print("Opss! Number is the same as Original number")
                    else:
                        print(f"Number is {'greater' if number - reference >= 0 else 'lesser'} than {reference}")

                    print(f"You have {question_left} Lefts")
                except:
                    print("Look like your reference is not a number. Please re enter")

            case 'multiple':
                if question_left <= 0:
                    print("You have no question left")
                    continue

                if len(cmd.split()) < 2:
                    print("Look like you only have \"multiple\", but not the factor number. Please re enter")
                    continue

                factor = cmd.split()[1]
                
                try:
                    factor = int(factor)

                    question_left -= 1

                    print(f"Number is {'not ' if number % factor != 0 else ''}multiple of {factor}")

                    print(f"You have {question_left} Lefts")
                except:
                    print("Look like your factor is not a number. Please re enter")

            case 'factor':
                if question_left <= 0:
                    print("You have no question left")
                    continue

                if len(cmd.split()) < 2:
                    print("Look like you only have \"factor\", but not the original number. Please re enter")
                    continue

                original = cmd.split()[1]
                
                try:
                    original = int(original)

                    question_left -= 1

                    print(f"Number is {'not ' if original % number != 0 else ''}factor of {original}")

                    print(f"You have {question_left} Lefts")
                except:
                    print("Look like your original is not a number. Please re enter")

if __name__ == "__main__":
        
    while True:
        one_game = input("One Game? (Y/N) : ")

        if len(one_game) == 0 or one_game[0].lower() in ['y', '1']:
            one_game = True
            break
        elif one_game[0].lower() in ['n', '0']:
            one_game = False
            break

        print("Please enter valid Input")

    if one_game:
        Game()
    else:
        score = 0
        end = False
        while not end:
            score += Game()

            while True:
                done = input("Done? (Y/N) : ")

                if len(done) == 0 or done[0].lower() in ['y', '1']:
                    end = True
                    break
                elif done[0].lower() in ['n', '0']:break

                print("Please enter valid Input")

        print(f"You've got {score} points")