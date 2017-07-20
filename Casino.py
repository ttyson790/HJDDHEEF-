balance = 1 
def restart() :
    global balance
    print ("Welcome to casino! You start with 1$ and your goal is to get 100$! Good luck!")   
    def start() :
        global balance
        game = input ("Please input which game you would like to play: [1] Coinflip [2] Roulette       [3] Dice")
        if game == "1":
            import random
            flip = (random.random())
            bet = input ("How much would you like to bet? Minimum: 0.1   ")
            bet = float(bet)

            if bet<= balance:   
                balance -= bet
                print ("Your balance is: ")
                print (balance)
            else:
                enter = input ("You don't have enough money. Press enter to go back or restart to restart.   ")
                if enter == (""):
                    start()
                elif enter == ("restart"):
                    restart()
                else:
                    print ("You didn't press enter")
                    enter = input ("Press enter to go back.   ")
                    if enter == (""):
                        start()
                    else:
                        print ("You didn't press enter or type restart, you have been redirected to the main menu.")
                        start()
                        
            enter = input ("Press enter to flip.   ")
            if enter == (""):
                if flip >= 0.5:
                    print ("You won!")
                    balance += bet * 1.95
                    print ("Your balance is: ")
                    print (balance)
                    enter = input ("Press enter to go back or type restart to restart.   ")
                    if enter == (""):
                        start()
                    elif enter == ("restart"):
                        restart()
                    else:
                        print ("You didn't press enter or write restart.")
                        enter = input ("Press enter to go back or type restart to restart.   ")
                        if enter == (""):
                            start()
                        elif enter == ("restart"):
                            restart()
                        else:
                            print ("You didn't press enter, you have been redirected to the main menu.")
                            start()
                else:
                    print ("You lost!")
                    print ("Your balance is: ")
                    print (balance)
                    cnrs = input ("Press any key to continue, type restart to restart.   ")
                    if cnrs == ("restart"):
                        restart()
                    else: start()
            else:
                print ("You didn't press enter.")
                enter = input ("Press enter to go back to the main menu.   ")
                if enter == (""):
                    start()
                else:
                    print ("You didn't press enter, you have been redirected to the main menu.")
                    start()
        elif game == "2":
            print ("Not avaliable yet.")
            start()
        elif game == "3":
            bet = input ("How much would you like to bet? Minimum: 0.1   ")
            bet = float(bet)  
            if bet<= balance:   
                balance -= bet
                print ("Your balance is: ")
                print (balance)
            else:
                enter = input ("You don't have enough money. Press enter to go back or restart to restart.   ")
                if enter == (""):
                    start()
                elif enter == ("restart"):
                    restart()
                else:
                    print ("You didn't press enter")
                    enter = input ("Press enter to go back.   ")
                    if enter == (""):
                        start()
                    else:
                        print ("You didn't press enter or type restart, you have been redirected to the main menu.")
                        start()
            multiplier = input("Please set your multiplier. x2, x3, x5, x10, x20")
            if multiplier == ("2" or "x2"):
                enter = input ("Press enter to roll.   ")
                if enter == (""):
                    if flip >= 0.5:
                        print ("You won!")
                        balance += bet * 1.95
                        print ("Your balance is: ")
                        print (balance)
                        enter = input ("Press enter to go back or type restart to restart.   ")
                        if enter == (""):
                            start()
                        elif enter == ("restart"):
                            restart()
                        else:
                            print ("You didn't press enter or write restart.")
                            enter = input ("Press enter to go back or type restart to restart.   ")
                            if enter == (""):
                                start()
                            elif enter == ("restart"):
                                restart()
                            else:
                                print ("You didn't press enter, you have been redirected to the main menu.")
                                start()
                    else:
                        print ("You lost!")
                        print ("Your balance is: ")
                        print (balance)
                        cnrs = input ("Press any key to continue, type restart to restart.   ")
                        if cnrs == ("restart"):
                            restart()
                        else:
                            start()
                
                
                
            '''print ("Not avaliable yet.")
            start()'''
        else:
            print ("You did not input a valid game number.")
            start()
    start()
restart()
        
    
