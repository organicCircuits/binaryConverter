#A simple program written in Python to convert decimal numbers to their binary equivalents using the standard formula: a[n]*2^n + a[n-1]*^(n-1)....a[0]*2^0.
#Many thanks to the authors of "The Binary System" webpage, Christing R. Wright and Samuel A. Rebelsky, for teaching me something new!
#Their website may be found at: http://www.math.grin.edu/%7Erebelsky/Courses/152/97F/Readings/student-binary

import math
from sys import stdin

x=0					                                        #Initializes the counter
exponential = math.pow(2,x)                                     #Converts the counter to a base 2 logarithm
A=[]                                                            #Creates an empty list to determine the highest value of P
binaryNumber = []                                               #Creates an empty list to create the binary equivalent of the user's decimal value

print('Please enter an integer greater than or equal to 0.')    #Asks the user to input desired decimal value

decimalNumber = int(stdin.readline())                           #The shell reads the user's decimal value

while decimalNumber > 0:                                #The while loop executes as long as the number to be converted is greater than 0

        exponential = math.pow(2,x)                             #Creates a seperate value for the exponential in the while loop
        if exponential <= decimalNumber:                        #If the log2 value is less than the original
                A.append(x)                                     #the value is added to list A
                x = x + 1                                       #and x is increased until you find the largest power of 2 less than the number being converted
        else:
                break                                           #If the power of 2 becomes larger than the number being converted, the loop ends

A.reverse()                                                     #A is reversed to determine last value of P calculated

x = A[0]                                                        #The last value of P is assigned to the exponential variable x

while x >= 0:                                                   #A while loop executes while x is greater than or equal to 0
        exponential = math.pow(2,x)                             #While in the loop, a new value is created for the power of x
        subtractee = decimalNumber - exponential                #A new variable is created to incrementally decrease the decimal value
        if exponential <= decimalNumber:                        #An if else loop is created to construct the binary number
                binaryNumber.append(1)                          #A one is entered if the log 2 value constructed from x is less than the decimal value
                decimalNumber = subtractee                      #And the number being converted becomes what was subtracted
                x = x-1                                         #The binary exponent is decreased until it reaches 0
        else:                                                   #If the exponential constructed is greater than the decimal number
                binaryNumber.append(0)                          #A '0' is appended to the binary number construct
                x = x-1                                         #and the binary exponent is still decreased until it reaches 0

print('The binary equivalent of that number is %s.') %binaryNumber      #the binary equivalent is created
