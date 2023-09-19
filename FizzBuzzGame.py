#The python codes for the famous fizz buzz game based on a simple children games Wikipedia : https://en.wikipedia.org/wiki/Fizz_buzz
# you can change the range of number which you want your program to run
# checking the first if statement is essential for the logic of this game
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
