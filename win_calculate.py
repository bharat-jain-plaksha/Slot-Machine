import spin
import os
import std_values
import numpy as np

class multiple:
    def __init__(self,spin_obj):
        self.spin_obj = spin_obj
        #self.spin_obj = spin.Spin() #To be removed and the spin object only to be passed in the main method. No new instances has to be created here
        self.values = std_values.Values()
        #os.system("clear")
        #self.spin_obj.rotate()
        self.all_3_list = self.values.all_3_list
        self.only_2_list = self.values.only_2_list
        self.only_1_list = self.values.only_1_list
        self.rewards = np.array([self.all_3_list,self.only_2_list,self.only_1_list])
    

    def calculate_multiple(self):
        a = self.spin_obj.nu_same()
        #print(a)
        if(a[0]<2):
            print("You won",self.rewards[a[0],a[1]],"times")
        return self.rewards[a[0],a[1]]

    

class balance_calculate:
    def __init__(self,balance,spin_amt,spin_obj) -> None:
        self.balance = balance 
        self.amt = spin_amt
        self.spin_obj = spin_obj
        self.multiple_obj = multiple(self.spin_obj)

    def deduction(self):
        self.balance = self.balance - self.amt

    def winnings(self): 
        multiple = self.multiple_obj.calculate_multiple()
        self.amt = self.amt*multiple
        print("You won:",self.amt)
    
    def balance_update(self):
        # self.balance_calculate.deduction()
        # self.balance_calculate.winnings()
        self.balance = self.balance + self.amt
        return self.balance
        
