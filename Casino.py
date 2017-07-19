
balance = 1
def restart() :
    print ("Welcome to casino! You start with 1$ and your goal is to get 100$! Good luck!")
    global balance
    balance = 1    
    def start() :
    
        game = input ("Please input which game you would like to play: [1] Coinflip   ")
        global balance
        if game == "1":
            import random
            flip = (random.random())
            bet = input ("How much would you like to bet? Minimum: 0.1   ")
            bet = float(bet)

            if bet <= balance:   
                balance -= bet
                print ("Your balance is: ")
                print (balance)
            else:
                print ("You don't have enough money")
                enter = input ("Press enter to go back, type restart to restart.   ")
                if enter == ("restart"):
                        restart()
                elif enter == (""):
                    start()
            
            enter = input ("Press enter to flip.")
            if enter == (""):
                if flip >= 0.5:
                    print ("You won!")
                    balance += bet * 1.95
                    print ("Your balance is: ")
                    print (balance)
                else:
                    print ("You lost!")
                    print ("Your balance is: ")
                    print (balance)
                    cnrs = input ("Press enter to continue, type restart to restart.   ")
                    if cnrs == ("restart"):
                        restart()
            else:
                print ("You didnt press enter")

            enter = input ("Press enter to go back")

            if enter == (""):
                start()
        else:
            print ("You didn't press enter")
    start()
restart()

