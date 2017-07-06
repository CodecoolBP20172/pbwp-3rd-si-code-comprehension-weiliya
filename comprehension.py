import random  # import the random modul 

guessesTaken = 0  # assign 0 to guesesTaken variable

print('Hello! What is your name?')  # prints to the console 'Hello! What is your name?'
myName = input() # asks the user for an input and assigns it to myName variable

number = random.randint(1, 20)  # randomly generates a number between 1 and 20 including 1 and 20 as well, random modul had to be imported to be able to use this
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # prints the text in the brackets and uses the input from user that has been assigned to myName

while guessesTaken < 6:  # this while loop runs until the condition guessesTaken < 6 is true, it it is false, the loop ends
    print('Take a guess.')  # prints to console till guessesTaken < 6
    guess = input()  # assigns user input to variable guess
    guess = int(guess)  # cast variable type guess to integer

    guessesTaken += 1   # adds 1 to variable guessesTaken each time the condition is true

    if guess < number:  # this if statement examines if the guess variable is smaller than the number variable, if this statement is true then
        print('Your guess is too low.')  # prints 'Your guess is too low.' to console

    if guess > number:  # if this statement (variable guess is bigger than variable number) is true then
        print('Your guess is too high.')  # prints 'Your guess is too high.' to console

    if guess == number:  # if statement 'variable guess equals to variable number' is true then
        break  # the break statement terminates the while loop and jumps to the next line of code after this block

if guess == number:  # if statement 'variable guess equals to variable number' is true then
    guessesTaken = str(guessesTaken)  # changes variable type guessesTaken to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # outputs the text in between the brackets and the user input assigned to variable myName

if guess != number:  # if statement 'guess is not equal to number' is true, then
    number = str(number)  # cast variable type number to string
    print('Nope. The number I was thinking of was ' + number)  # prints the text and the string value of number variable to the console
