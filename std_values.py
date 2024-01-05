#to store all the std values of the game here, and can be changed from here to all the places 
#in the code

class Values:
    def __init__(self) -> None:
        
        #win
        self.all_3_list = [50,40,30,10,5]
        self.only_2_list = [7,5,3,2,1.5]
        self.only_1_list = [0,0,0,0,0]

        #Game 
        self.opts = ["💸","🪙","🍎","🥝","🍓"]
        self.names = ["Money","Coin","Apple","Kiwi","Strawberry"]

        #Bias
        self.bias = [0.10,0.15,0.20,0.25,0.3]
        self.index = [0,1,2,3,4]
        self.seq = ["Null","Null","Null"]

