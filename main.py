import time
import spin 
import std_values
import welcome_msg
import win_calculate
import os
import time
import amt_to_word

"""
Apple 🍎
Kiwi 🥝
Strawberry 🍓
Cash 💸
Coin 🪙

7 combinations
Get all Cash for Highest 
"""

os.system("clear")
acc_bal = 1000
acc_bal = int(input("Enter the amount you want to play with today!"))
welcome_msg.wel_msg()
time.sleep(1)
print("Let's Play:")
while acc_bal>=0:
    #play_amt = 100
    play_amt = int(input("Enter Bet Amount:"))
    spin_obj = spin.Spin()
    spin_obj.rotate()
    spin_obj.print_seq()
    #spin_obj.print_names()
    calc_obj = win_calculate.balance_calculate(acc_bal,play_amt,spin_obj)
    calc_obj.deduction()
    calc_obj.winnings()
    acc_bal = calc_obj.balance_update()
    print("New Balance:",acc_bal)
    amt_to_word.MainFunc(acc_bal)
    print()
