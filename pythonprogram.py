# Python Program to print Strong Numbers from 1 to Nth Number

# Import Module
import math

minValue = 1
maxValue =  5000

totalStrongNo = 0

for Number in range(minValue, maxValue):
    Temp = Number
    Sum = 0
    while(Temp > 0):
        Reminder = Temp % 10
        Factorial = math.factorial(Reminder)
        Sum = Sum + Factorial
        Temp = Temp // 10

    if (Sum == Number):
        print("%d is a Strong Number" %Number)
        totalStrongNo = totalStrongNo + 1

if(totalStrongNo==0):
    print("\nThere is No Strong Number Between {0} and {1}".format(minValue,maxValue))
