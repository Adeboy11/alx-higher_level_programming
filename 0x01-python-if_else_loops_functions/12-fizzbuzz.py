#!/usr/bin/python3
"""Print the nos from 1 to 100.
  For multiples of 3, prints FIZZ
  For multiples of 5, prints BUZZ
  For multiples of 3 and 5, prints FIZZBUZZ
  """

def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
