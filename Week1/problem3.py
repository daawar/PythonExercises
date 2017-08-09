# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 23:33:36 2017

@author: daawar.khan
"""

"""
Problem 1_3:  
Write a function problem1_3(n) that adds up the numbers 1 through n and
prints out the result. You should use either a 'while' loop or a 'for' loop.
Be sure that you check your answer on several numbers n.  Be careful that your
loop steps through all the numbers from 1 through and including n.

Tip: As this involves a loop you could make an error that causes it to run 
forever. Usually Control-C will stop it. See suggestions at the beginning of 
this document.  With loops take care that your first and last iterations are
what you expect. A print statement can be inserted in the loop to monitor it, 
but be sure this isn't in the submitted function.
"""
#%%
def problem1_3(n):
    my_sum = 0
    current_number = 1
    while current_number<=n:
        my_sum = my_sum + current_number
        current_number = current_number + 1
        
    print(my_sum)
    


