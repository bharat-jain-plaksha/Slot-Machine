import time
def print_rewards():
    print("Get: \n💸💸💸-->50X\n🪙🪙🪙 -->40X\n🍎🍎🍎-->30X\n🥝🥝🥝-->10X\n🍓🍓🍓-->5X")

def wel_msg():
    wel_msg = ("Welcome: This is Slot Machine. Win upto 50X of your money!")
    wel_msg = wel_msg.split()


    for i in wel_msg: 
        time.sleep(0.2)
        print(i," ",end="",flush=True)

    print("\nHere are the Jackpots:")

    #ch = bool(input("Here are the Jackpots:"))
    time.sleep(0.5)
    print_rewards()