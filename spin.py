import random
import os
#Random Spinning the function and giving a combination of the same. 
class Spin:
    def __init__(self):
        self.opts = ["💸","🪙","🍎","🥝","🍓"]
        self.names = ["Money","Coin","Apple","Kiwi","Strawberry"]
        self.order = []
        self.bias = [0.10,0.15,0.20,0.25,0.3]
        self.index = [0,1,2,3,4]
        self.seq = ["Null","Null","Null"]
    
    def rotate(self):
        self.seq = random.choices(self.index,weights=self.bias,k=3)
        return self.seq

    def print_seq(self):
        [print(self.opts[i],end=" ",flush=True) for i in self.seq]
        print()
    
    def get_seq(self):
        return self.seq
    
    def change_bias(self,bias):
        self.bias  = bias
    
    def print_names(self):
        [print(self.names[i],end=" ",flush=True) for i in self.seq]
        print()
    
    def nu_same(self) -> list:
        if (all(i == self.seq[0] for i in self.seq)):#all_3
            print("Mega Jackpot!!!")
            return [0,self.seq[0]]
        elif(self.seq[0] == self.seq[1] or self.seq[1] == self.seq[2] or self.seq[0] == self.seq[2]):#only 2
            print("Very Close to Jackpot")
            if(self.seq[0]==self.seq[1] or self.seq[0]==self.seq[1]):
                return [1,self.seq[0]]
            else:
                return [1,self.seq[1]]
        else:
            print("No Win,Sorry")
            if(any(i==0 for i in self.seq)):
                return [2,0]
            else:
                return [2,1] 
    
    # def nu_same(self) -> dict:
    #     #returns the frequency of elements in a dictionry 
    #     self.freq = dict()     
    #     for i in self.names:
    #         self.names = 

            









    # def print_all(self):
    #     print_seq()

    


    
# a = "U+1F34E" #apple
# chr_int = int(a[2:],16)
# print("int=", chr_int)
# print(chr(chr_int))
# names = ["Money","Coin","Apple","Kiwi","Strawberry"]
# opts = ["💸","🪙","🍎","🥝","🍓"] #They are characters and needed to be stored like one in "", not standalone, it is like stroning name = bharat --> ob. wrong. still it is a character!!!!!!! I wasted too much time on this? 


# [print(fruit) for fruit in opts]

# # b = "\U0001F34E" #apple 
# # a = a.replace("+","000")

# #a = "\\" + a

# a = a.encode("utf-8")
# # c = "\x55\x30\x30\x30\x31\x46\x33\x34\x45"

# print(    # def nu_same(self) -> dict:
    #     #returns the frequency of elements in a dictionry 
    #     self.freq = dict()     
    #     for i in self.names:
    #         self.names = 

            


    