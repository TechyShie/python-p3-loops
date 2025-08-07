#!/usr/bin/env python3
# happy new year
def happy_new_year():
    x = 10
    while x <= 10 and x > 0:
        print(x)
        x -= 1
    else:
        print("Happy New Year!")

happy_new_year()


#square integers
def square_integers(int_list):
    results = []
    for i in int_list:
        results.append(i ** 2)
    return results

square_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
 

    

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
 
