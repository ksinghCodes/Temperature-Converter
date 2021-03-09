#!/usr/bin/env python 3.7


# python implementation goes here

#get input and cast to float
fahrenheit = float(input("What tempereature in Fahrenheit would you like converted to Celsius? "))

#convert
celsius=(fahrenheit-32) * 5 / 9

#print and round
print(fahrenheit, "F is ", round(celsius,2), "C")
