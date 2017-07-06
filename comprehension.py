import random  # import the random modul to use its functions e.g. randint to be able to generate random numbers in the code 

guessesTaken = 0  # assign 0 to guesesTaken variable

print('Hello! What is your name?')  # prints to the console 'Hello! What is your name?'
myName = input() # asks the user for an input and assigns it to myName variable

number = random.randint(1, 20)  # randomly generates a number between 1 and 20 including 1 and 20 as well, random modul had to be imported to be able to use this
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # prints the text in the brackets and uses the input from user that has been assigned to myName

while guessesTaken < 6:  # this while loop runs until the condition guessesTaken < 6 is true, it it is false, the loop ends
    print('Take a guess.')  # prints to console till guessesTaken < 6
    guess = input()  # assigns user input to variable guess
    guess = int(guess)  # change variable type guess to integer

    guessesTaken += 1   # adds 1 to variable guessesTaken each time the condition is true

    if guess < number:  #
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
