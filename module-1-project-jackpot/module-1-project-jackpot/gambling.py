import random
MIN_BET = 1
MAX_BET = 100
ArcadeMachine = [
    ["❤️" , "🗝️" , "💵"],
    ["❤️" , "🗝️" , "💵"],
    ["❤️" , "🗝️" , "💵"],
]
dep = False
def runMachine(game) : 
    results = list()
    for thing in game : 
        rand = random.randint(0 , 2)
        results.append(thing[rand])
    return results

def deposit() : 
    while True : 
        amount = input("Enter the Amount to be Deposited $")
        if amount.isdigit() : 
            amount = int(amount)
            if amount > 0 : 
                break
            else : 
                print("Amount Should be greater than zero!!")
        else : 
            print("Invalid Amount !! Please Enter a valid Amount")
    return amount


def get_bet() : 
    while True : 
        bet = input(f"How much you like to bet  (${MIN_BET} - ${MAX_BET}) $")
        if bet.isdigit() : 
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET : 
                break
            else : 
                print(f"bet should be in {MAX_BET} - {MIN_BET}")
        else : 
            print("Invalid Input !! Please Enter a valid bet")
    return bet
def check_for_prize(gameresults) : 
    won = True 
    first = gameresults[0]
    for value in gameresults : 
        if value != first : 
            won = False
            return [won , first]
    if (won and first == "❤️") : 
        return [won , 15]
    elif (won and first == "🗝️") : 
        return [won , 30]
    else : 
        return [won , 50]
    

def main() :     
    global dep , BALANCE
    if not  dep : 
        BALANCE = deposit()
    bet = get_bet()
    if bet <= BALANCE : 
        machine_results = runMachine(ArcadeMachine)
        print("Results : " , machine_results)
        winCheck = check_for_prize(machine_results)
        if(winCheck[0]) : 
            print(f"Congratulations You Have Won!! +${winCheck[1]*100 / bet}")
            BALANCE += winCheck[1]*100 / bet
            print("Current Balance : ", BALANCE)
        else : 
            print(f"Sorry, Better Luck Next Time -${bet}")
            BALANCE -= bet
            print("Current Balance : " , BALANCE)
    else : 
        print("Your don't have Enough Money to Bet! Deposit Money to Continue : \n")
        choice = input("1 -> Deposit \n2 -> quit : ")
        if int(choice) == 1 : 
            dep = False
            main()
        else : 
            quit() 

    choice = input("Do you want to bet again? : ")
    if choice == "yes" : 
        dep =  True
        main()
    else : 
        print("thank you for playling Arcade Game")
        quit()
main()