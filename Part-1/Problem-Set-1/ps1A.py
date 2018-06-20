# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 21:53:15 2017

@author: Salmane Tamo
Problem set #1A
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream house: "))

r = 0.04
portion_down_payment = 0.25
current_savings = 0.0
number_of_months = 0

while (portion_down_payment*total_cost) >= current_savings:
    current_savings += (portion_saved*annual_salary/12) + current_savings*r/12
    number_of_months += 1
print("Number of months: ", number_of_months)