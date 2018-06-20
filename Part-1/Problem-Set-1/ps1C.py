# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 23:12:03 2017

@author: Salmane Tamo
"""

annual_salary = float(input("Enter your annual salary: "))

def get_best_savings_rates(starting_salary):
    """
    Input: starting_salary, a float
    Uses bisection to approximate the best savings rate to within 100$
    Returns: a float approximating the best savings rate
    """
    total_cost = 1000000.0
    semi_annual_raise = .07
    r = 0.04
    portion_down_payment = 0.25
    current_savings = 0.0
    number_of_months = 0
    number_of_steps = 0
    
    low = 0.0
    high = 1.0
    guess = (low + high)/2.0
    while not(portion_down_payment*total_cost - 100 < current_savings and portion_down_payment*total_cost + 100 > current_savings):
        down_payment_possible = True
        current_savings = 0.0
        number_of_months = 0
        temp_starting_salary = starting_salary
        accumulated_salary = starting_salary
        while number_of_months < 37:
            current_savings += (guess*temp_starting_salary/12) + current_savings*r/12
            number_of_months += 1
            if number_of_months%6 ==0:
                temp_starting_salary += temp_starting_salary*semi_annual_raise
            accumulated_salary += temp_starting_salary/12    
        if current_savings < portion_down_payment*total_cost - 100:
            if accumulated_salary < portion_down_payment*total_cost - 100:
                down_payment_possible = False
                break                
            low = guess
        elif current_savings > portion_down_payment*total_cost + 100:
            high = guess
        guess = (high + low)/2.0
        number_of_steps += 1
    if not down_payment_possible:
        print("It's not possible to pay the down payment in 36 months")
    else:
        print("Best savings rate: ",guess)
        print("Number of steps in bisection search: ", number_of_steps)
    return guess


z = get_best_savings_rates(annual_salary)
print(z)