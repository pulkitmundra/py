#!/usr/bin/python2
def factorial(num):
	if num==1:
		return num
	else:
		return num*factorial(num-1)
num= input("enter no.")
if num < 0:
	print("fact cannot be of negetive no.")
elif num==0:
	print("fact is 1")	
else:
	print("fact of the given no. is " ,factorial(num))
