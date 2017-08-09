# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 23:39:42 2017

@author: daawar.khan
"""

"""
Problem 1_5:
Write a function 'problem1_5(age)'. This function should use if-elif-else
statement to print out "Have a glass of milk." for anyone under 7; "Have
a coke." for anyone under 21, and "Have a martini." for anyone 21 or older.

Tip: Be careful about the ages 7 (a seven year old is not under 7) and 21.
Also be careful to make the phrases exactly as shown for the auto-grader.
"""
#%%
def problem1_5(age):

    message_for_under7 = "Have a glass of milk."
    message_for_under21 = "Have a coke."
    message_for_above21 = "Have a martini."
    
    if age<7:
        print(message_for_under7)
        
    elif age<21:
        print(message_for_under21)
        
    else:
        print(message_for_above21)
        
