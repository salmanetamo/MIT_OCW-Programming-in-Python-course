# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:54:48 2017

@author: Salmane Tamo
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream house: "))
semi_annual_raise = float(input("Enter your semi annual raise, as a decimal: "))

r = 0.04
portion_down_payment = 0.25
current_savings = 0.0
number_of_months = 0

while (portion_down_payment*total_cost) >= current_savings:
    current_savings += (portion_saved*annual_salary/12) + current_savings*r/12
    number_of_months += 1
    if number_of_months%6 ==0:
        annual_salary += annual_salary*semi_annual_raise
print("Number of months: ", number_of_months)