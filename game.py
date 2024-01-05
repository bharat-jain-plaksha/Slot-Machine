import spin 
class game:
    def __init__(self,balance):
        self.balance = balance

    def spin(self):
        obj = spin.Spin
        while (self.balance>=1000):
            obj.rotate()
            seq = obj.get_seq

            
            
