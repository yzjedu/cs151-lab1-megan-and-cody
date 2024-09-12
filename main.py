# Programmers: Cody and Megan
# Course: CS 151 Dr. Zelalem Yalew
# Due Date: 9/18/2024
# Lab Assignment: 1
# Problem Statement: Convert Miles, MPG, Gas Cost to Cost for the entire trip
# Data In: Miles, MPG, Gas Cost
# Data Out:  Cost for trip
# Credits: Lab 1

#This program converts miles, mpg, and cost of gas, to find the total cost for the entire trip

miles_str = input('Enter the number of miles in the trip')
miles_int = int(miles_str)
mpg_str = input('Enter the number of mpg')
mpg_int = int(mpg_str)
cost_of_gas_str = input('Enter the cost of gas')
cost_of_gas_int = int(cost_of_gas_str)

cost_of_trip =(miles_int / mpg_int) * cost_of_gas_int

print("The cost of the trip is", cost_of_trip)