#1 Write a python script for conversion which accepts distance in km convert to miles, accept temperature in Celsius and convert to Fahrenheit and also accepts time in minutes and convert it to seconds. 

#km to miles
k=int(input("enter a kilometer"))
miles=k*0.62
print("the kilometer in miles is",miles)

#celsius to fahrenheit
c=int(input("enter a celsius :"))
fah=c*5/9+32
print("celsius in fahrenheit",fah)
#minutes to second
m=int(input("enter a minutes"))
sec=m*60
print("minutes in second :",sec)

