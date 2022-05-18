def rockpaperscissors():
    global winner
    global loser
    global a1
    global b1
    a1 = str(input("Player1 enter your name: ")).upper()
    a = str(input(f"{a1}, enter first move: "))
    b1 = str(input("Player2 enter your name: ")).upper()
    b = str(input(f"{b1}, enter your move: "))

    if a == "rock" and b == "scissors":
        winner = a1
        loser = b1
        print(f"{winner} played scissors and wins")
    else:
        if a == "scissors" and b == "rock":
            winner = b1
            loser = a1
            print(f"{winner} played rock and wins")

    if a == "paper" and b == "rock":
        winner = a1
        loser = b1
        print(f"{winner} played paper and wins")
    else:
        if a == "rock" and b == "paper":
            winner = b1
            loser = a1
            print(f"{winner} played paper and wins")

    if a == "paper" and b == "scissors":
        winner = b1
        loser = a1
        print(f"{winner} played scissors and wins")
    else:
        if a == "scissors" and b == "paper":
            winner = a1
            loser = b1
            print(f"{winner} played scissors and wins")

    if a == "paper" and b == "paper":
        print(f"{a1} draws {b1}")
    if a == "rock" and b == "rock":
        print(f"{a1} draws {b1}")
    if a == "scissors" and b == "scissors":
        print(f"{a1} draws {b1}")
def guesser():
    usd_exchange = {"USD": 1, "GBP": 0.76, "JPY": 123.82, "NGN": 415.72}
    host = input("Host enter your name: ").title()
    host_currency = input(f"Choose preferred currency from: {usd_exchange.keys()}").upper()
    guest = input("Guest pls enter your name: ").title()
    guest_currency = input(f"Choose preferred currency from: {usd_exchange.keys()}").upper()

    host_turn = int(input(f"{host}, pick a number within 1-10: "))
    guest_turn = int(input(f"{guest}, now you guess what number {host} picked from 1-10: "))
    trials = 1
    def curr_convrtr (currency, amount):
        rate = usd_exchange[currency]
        winnings = amount * rate
        return(winnings)


    winner = None
    while trials < 3:
        if (host_turn == guest_turn) and (trials == 1):
            winner = guest
            print(f"Congratulations {winner}")
            print(f"{host}, please pay {guest} {guest_currency} {curr_convrtr(guest_currency, 50)}")
            break
        elif (host_turn == guest_turn) and (trials == 2):
            winner = guest
            print(f"Congratulations {winner}")
            print(f"{host}, please pay {guest} {guest_currency} {curr_convrtr(guest_currency, 25)}")
            break
        elif (host_turn == guest_turn) and (trials == 3):
            winner = guest
            print(f"Congratulations {winner}")
            print(f"{host}, please pay {guest} {guest_currency} {curr_convrtr(guest_currency, 5)}")
            break

        else:
            if trials == 3:
                print(f"{host} wins this round!!!")
            else:
                guest_turn = int(input("Sorry try again: "))
                winner = host
                trials = trials + 1

    if winner == guest:
        print(f"Good job {guest}")
    else:
        print(f"{guest} please pay {host} {host_currency} {curr_convrtr(host_currency, 75)}")
        print(f"Congratulations {host}")
def sec_guesser():
    usd_exchange = {"USD": 1, "GBP": 0.76, "JPY": 123.82, "NGN": 415.72}
    host = winner
    host_currency = input(f"{host}, Choose preferred currency from: {usd_exchange.keys()}").upper()
    guest = loser
    guest_currency = input(f"{guest}, Choose preferred currency from: {usd_exchange.keys()}").upper()

    host_turn = int(input(f"{host}, pick a number within 1-10: "))
    guest_turn = int(input(f"{guest}, now you guess what number {host} picked from 1-10: "))
    trials = 1

    def curr_convrtr(currency, amount):
        rate = usd_exchange[currency]
        winnings = amount * rate
        return (winnings)

    sec_gameWinner = None
    while trials < 3:
        if (host_turn == guest_turn) and (trials == 1):
            sec_gameWinner = guest
            print(f"Congratulations {sec_gameWinner}")
            print(f"{host}, please pay {guest} {guest_currency} {curr_convrtr(guest_currency, 50)}")
            break
        elif (host_turn == guest_turn) and (trials == 2):
            sec_gameWinner = guest
            print(f"Congratulations {sec_gameWinner}")
            print(f"{host}, please pay {guest} {guest_currency} {curr_convrtr(guest_currency, 25)}")
            break
        elif (host_turn == guest_turn) and (trials == 3):
            sec_gameWinner = guest
            print(f"Congratulations {sec_gameWinner}")
            print(f"{host}, please pay {guest} {guest_currency} {curr_convrtr(guest_currency, 5)}")
            break

        else:
            if trials == 3:
                print(f"{host} wins this round!!!")
            else:
                guest_turn = int(input("Sorry try again: "))
                sec_gameWinner = host
                trials = trials + 1

    if sec_gameWinner == guest:
        print(f"Good job {guest}")
    else:
        print(f"{guest} please pay {host} {host_currency} {curr_convrtr(host_currency, 75)}")
        print(f"Congratulations {host}")


import sys
global a1
global b1
global winner
global loser
global host
global guest
def worldofgames():

     def newgame():
         print('''Hey there, welcome to world of games!!!
            #  You can choose between a game of Number Guessing or Rock-Paper_Scissors.''')
         t = int(input("\nType in '1' for Number Guessing and '2' for Rock-Paper-Scissors:  "))

         if t == 1:
             print("First, we play Rock-Paper-Scissors to decide who goes first")
             rockpaperscissors()
             sec_guesser()
             s = input("Would you like to play again? 'y' for Yes and 'n' for No: ")
             while s == "y":
                 sec_guesser()
             else:
                 if s == "n":
                     sys.exit()

         if t == 2:
             guesser()
             r = input("Would you like to play again? 'y' for Yes and 'n' for No: ")
             while r == "y":
                 guesser()
             else:
                 if r == "n":
                     sys.exit()

         #  game = input("Hello, are you up for a game? Pls select 'y' for Yes and 'n' for No:   ")
         #  while game == "y":
         #      guesser()
         #  else:
         #     if game == "y":
         #         sys.exit()
         # if game == "n":
         #     sys.exit()
         # while game != "y" and game != "n":
         #     game = str(input("Incorrect entry, please retry: "))








            # if a == "rock" and b == "scissors":
            #     winner = b1
            #     loser = a1
            #     print(f"{winner} played scissors and wins")
            # if a == "rock" and b == "paper":
            #     winner = b1
            #     loser = a1
            #     print(f"{winner} played rock loses")
            # if a == "rock" and b == "rock":
            #     print("draw")
            # if a == "paper" and b == "rock":
            #     print("paper wins")
            # if a == "paper" and b == "scissors":
            #     print("paper loses")
            # if a == "paper" and b == "paper":
            #     print("draw")
            # if a == "scissors" and b == "paper":
            #     print("scissors wins")
            # if a == "scissors" and b == "rock":
            #     print("scissors loses")
            # if a == "scissors" and b == "scissors":
            #     print("draw")
     newgame()
worldofgames()