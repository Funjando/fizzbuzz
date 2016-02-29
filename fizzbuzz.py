"""
fizzbuzz.py
Author: Funjando
Credit: 

Assignment:

Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for 
the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.

We will use a variation of this test in which the last number of 
the series isn't necessarily 100, and the two numbers being tested 
for multiples aren't necessarily three and five. For example, your 
program should behave just like this:

How many numbers shall we print? 25
For multiples of what number shall we print 'Fizz'? 3
For multiples of what number shall we print 'Buzz'? 5
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
"""




#inputs
nr_nr=int(input("How many numbers shall we print? "))
fizz=int(input("For multiples of what number shall we print 'Fizz'? "))
buzz=int(input("For multiples of what number shall we print 'Buzz'? "))

fizz_list=range(0, nr_nr*fizz, fizz)
buzz_list=range(0, nr_nr*buzz, buzz)

t= [x for x in range(1, nr_nr+1)]
for x in t:
        if x in fizz_list and x in buzz_list:
            print("FizzBuzz")
        elif x in fizz_list:
            print("Fizz")
        elif x in buzz_list:
            print("Buzz")
        else:
            print(x)
