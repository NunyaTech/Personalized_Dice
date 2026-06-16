import random
import time
import sys
Greet = input("<none of this info is shared> What is your name?:")
ask = int(input(f"Hello {Greet}, what would you like the minimum number to be on your dice?<Whole numbers Only>"))
ask2 = int(input(f"Okay {Greet}, now what would you like the maximum number to be on your dice?<Whole numbers Only>"))
random_number = random.randint(ask, ask2)
ask3 = input("Would you like to roll? <y/n/Y/N>")
if ask3 == "Y" or ask3 == "y":
    print("Rolling...")
    time.sleep(3)
    print(random_number)
elif ask3 == "N" or ask3 == "n":
    print("Okay, you just wasted your time!\nClosing app...")
    time.sleep(3)
    sys.exit()
else:
    print("Invalid Input")