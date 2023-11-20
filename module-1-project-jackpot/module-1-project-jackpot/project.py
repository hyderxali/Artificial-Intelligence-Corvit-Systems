import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap  as tb
from tkinter import messagebox
import random
import collections



def startJackPotGameGUI(username , cash , accroot):
    accroot.destroy()
    root = tb.Window(title="JackPot Game" , themename="litera")
    root.geometry("800x800")
    btn_style = tb.Style()
    btn_style.configure(".TButton" , font=("Helvatica" , 16)) 
    lbl_style = tb.Style()
    lbl_style.configure(".TLabel" , font=("Helvatica" , 14))
       
    game_label = tb.Label(root , text=f"Welcome Back {username} To the JackPot Game" , font=("monospace" , 18))
    
    game_label.pack(pady=5)
    notebook = tb.Notebook(root , bootstyle="dark")
    notebook.pack(fill=X , padx=20)

    deposit_cash = tb.Frame(notebook)
    play = tb.Frame(notebook)
    
    back = tb.Button(root , text="Accounts" , command=user_accountsGUI)
    back.pack(anchor="ne", padx=20, pady=10)
    
    Account_status = tb.Label(play, text=f"Account Status : {cash}$")
    Account_status.pack(anchor="ne", padx=20, pady=10)
    deposit_label = tb.Label(deposit_cash , text="Enter the cash amount to deposit(1$-100): " ,style="Tlabel")
    deposit_label.pack(fill=X , padx=10)
    deposit_entry = tb.Entry(deposit_cash)
    deposit_entry.pack(fill=X, padx=10)

    deposit_btn = tb.Button(deposit_cash , style="TButton",text="Deposit" , command= lambda : (depositCash(deposit_entry.get() , username), updateAccountStatus(Account_status , username)))
    
    deposit_btn.pack(fill=X, padx=10 , pady=5)
    
    notebook.add(deposit_cash , text="Deposit")
    game_cell_one = tb.Label(play , text="#" , font=("monospace" , 26))
    game_cell_two = tb.Label(play , text="#", font=("monospace" , 26))
    game_cell_three = tb.Label(play , text="#", font=("monospace" , 26))
    game_cell_four = tb.Label(play , text="#", font=("monospace" , 26))
    
    game_cell_one.pack()
    game_cell_two.pack()
    game_cell_three.pack()
    game_cell_four.pack()
    bet_label = tb.Label(play , text="Enter the Amount you want to bet$ : " , style="TLabel")
    bet_label.pack()
    bet_entry = tb.Entry(play)
    bet_entry.pack()
    bet_button = tb.Button(play , text="Bet" , style="TButton", command= lambda : (bet(bet_entry.get() , username , game_cell_one , game_cell_two , game_cell_three , game_cell_four , root , Account_status)))
    bet_button.pack(fill=X)
    notebook.add(play , text="Play")
    
    root.mainloop()
    
   
def bet(bet , username , one , two ,three , four , play , label):
    f = open("accounts.txt" , "r")
    try:         
        bet = float(bet)
    except:
        messagebox.showerror("Error" , "Please enter an integer Value")
        return
    for line in f:
        try : 
            user , passw , money = line.strip().split(":")
        except:
            continue
        if user == username :
            if float(bet) < 1 : 
                messagebox.showerror("Error!" , "Bet can't be 0 or less than zero")
            elif float(bet) > float(money) : 
                messagebox.showerror("Error!" , f"In Sufficient Balance bet can't be more than {money}$")
            else :
                spinJackpot(one ,two , three , four , play , bet, username , label)

def spin(label, count, play, callback , username , ulabel):
    def spin_iteration(i):
        if i < count:
            update_label(label)
            play.after(100, spin_iteration, i + 1)
        else:
            callback(label.cget("text"), username , ulabel)

    spin_iteration(0)

def spinJackpot(one, two, three, four, play, bet , username , label):
    result = [None, None, None, None]
    count = 0

    def spin_callback(value , username , label):
        nonlocal count
        result[count] = value
        count += 1
        if count == 4:
            # All spins completed
            gameResults(result , bet , username , label)

    spin(one, 9, play, spin_callback, username , label)
    spin(two, 18, play, spin_callback , username , label)
    spin(three, 29, play, spin_callback , username , label)
    spin(four, 45, play, spin_callback , username , label)

    return result
                                                
def gameResults(symbols,bet , username , label):
    print(symbols)
    symb = collections.Counter(symbols)
    if len(symb) == 1 : 
        messagebox.showinfo("Congratulations!" , f"You have won{bet}$ , play again to win more")
        updateMoneyAfterBet(username , bet , 2 , label)
    elif len(symb) == 2 : 
        messagebox.showinfo("Congratulations!" , f"You have won{bet*0.5}$ , play again to win more")
        updateMoneyAfterBet(username , bet , 1.5 , label)
        
    elif len(symb) == 3 :
        messagebox.showinfo("OH NO!" , f"You have lost{bet*0.5}$ , better luck next time")
        updateMoneyAfterBet(username , bet , 0.5 , label)
    else : 
        messagebox.showinfo("OH NO!" , f"You have all lost the betting amount {bet}$ , better luck next time")
        updateMoneyAfterBet(username , bet , 0 , label)
        
        
def updateMoneyAfterBet(accountName , bet , prize , label):
    with open("accounts.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(lines):
            try : 
                user , passw , money = line.strip().split(":")
            except:
                continue
            if user == accountName:
                lines[i] = f"{user}:{passw}:{float(money)-float(bet)+(float(bet) * prize)}\n"
                f.writelines(lines)
                break
    updateAccountStatus(label , accountName)
    
def getRandomSymbol():
    symbols = ["❤️" , "🗝️" , "💵", "💎"]   
    return random.choice(symbols)
    
def update_label(label):
    symbol = getRandomSymbol()
    label.config(text=symbol)


def updateAccountStatus(label , username):
    f = open("accounts.txt" , "r")
    for line in f:
        try : 
            user , passw , money = line.strip().split(":")
        except:
            continue
        if user == username : 
            label.config(text  = f"Account Status : {money}$")
    f.close()
            
            
def depositCash(cash, accountName):
    try:
        cash = float(cash)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number instead of a string")
        return

    if not (1 <= cash <= 100):
        messagebox.showerror("Error", "The range is between $1 and $100 only!")
        return

    with open("accounts.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(lines):
            try:
                user, passw , money = line.split(":")
            except:
                continue
            if user == accountName:
                lines[i] = f"{user}:{passw}:{float(money)+float(cash)}\n"
                messagebox.showinfo("Success", f"${cash} has been deposited to {accountName}'s account")
                f.writelines(lines)
                break
    
def getLoginData(username , password , root):
    username_results  = validateUserName(username)
    f = open("accounts.txt" , "r")
    found = False
    if not username_results:
        for line in f:
            try:
                user, passw , cash = line.split(":")
            except:
                continue
            if user == username:
                found = True
                if passw == password : 
                    messagebox.showinfo("Success!" , "Logged in successfully")
                    startJackPotGameGUI(username , cash , root)
                    break
                else : 
                    messagebox.showerror("Error!" , "Invalid passowrd entered")
    if not found : 
        messagebox.showerror("Error!" , "User not Found!")
                              

def getRegistrationData(username , password , conf_password):
    username_results , password_results = validateUserName(username , "reg") , validatePassowrd(password)
    f = open('accounts.txt' , 'a')
    if not username_results and not password_results : 
        if password == conf_password:

                f.write(f"{username}:{password}:0\n")
                messagebox.showinfo("Success!" , "Account Created Successfully!")
                f.close()
                
        else:
            messagebox.showerror("Error!" , "Password does not match!")
    
def validateUserName(username , reg = ""):
    errors = list()
    f = open("accounts.txt" , "r")
    if username[0].isnumeric() and username[0].isalnum():
        errors.append("Username cannot start with a number or special character")
        messagebox.showerror("Error!","Username cannot start with a number or special character")
    if " " in username:
        errors.append("Username can't contain a space")
        messagebox.showerror("Error!" , "Username can't contain a space")
    if(reg!=""):
        for line in f :
            try: 
                user , passw , cash = line.strip().split(":")
            except:
                continue
            if user == username:
                errors.append(f"User : {username} already exists")
                messagebox.showerror("Error!" , f"User : {username} already exists")
            
    return errors

    
        
def validatePassowrd(password):
    u = d = False
    errors = list()
    if len(password) < 8 : 
        errors.append("Passoword should be alleast 8 character long")
        messagebox.showerror("Error!" , "Passoword should be alleast 8 character long" )
    for i in password : 
        if i.upper() == i:
            u = True
        if i.isdigit() or not i.isalnum():
            d = True
    if not u:
        errors.append("password should contain at least one uppercase letter")
        messagebox.showerror("Error!" , "password should contain at least one uppercase letter")
        
    if not d:
        errors.append("password should contain atleast one digit or special character")
        messagebox.showerror("Error!" , "password should contain atleast one digit or special character" )
        
    return errors



def user_accountsGUI():
    root = tb.Window(title="Accounts" , themename="litera")
    root.geometry("800x800") 
    btn_style = tb.Style()
    btn_style.configure(".TButton" , font=("Helvatica" , 16)) 
    lbl_style = tb.Style()
    lbl_style.configure(".TLabel" , font=("Helvatica" , 10))
      
    notebook = tb.Notebook(root)
    notebook.pack(fill=X , padx=20 , pady=25)

    login_tab = tb.Frame(notebook)
    register_tab = tb.Frame(notebook)

    #login Tab
    username_label = tb.Label(login_tab , text="Username : " , style=".TLabel")
    username_label.pack(fill=X , padx=10)
    username_entry = tb.Entry(login_tab)
    username_entry.pack(fill=X, padx=10)

    password_label = tb.Label(login_tab , text="Password : ", style=".TLabel")
    password_label.pack(fill=X, padx=10)
    password_entry = tb.Entry(login_tab)
    password_entry.pack(fill=X, padx=10)

    submit_btn = tb.Button(login_tab, text="Submit" ,style=".TButton", command= lambda : getLoginData(username_entry.get() , password_entry.get() , root))
    submit_btn.pack(fill=BOTH, padx=10 , pady=20)
    #Register Tab
    new_username_label = tb.Label(register_tab , text="Username : ", style=".TLabel")
    new_username_label.pack(fill=X , padx=10)
    new_username_entry = tb.Entry(register_tab)
    new_username_entry.pack(fill=X, padx=10)

    new_password_label = tb.Label(register_tab , text="Create Password : ", style=".TLabel")
    new_password_label.pack(fill=X, padx=10)
    new_password_entry = tb.Entry(register_tab)
    new_password_entry.pack(fill=X, padx=10)


    confirm_password_label = tb.Label(register_tab , text="Confirm Password : ")
    confirm_password_label.pack(fill=X, padx=10)
    confirm_password_entry = tb.Entry(register_tab)
    confirm_password_entry.pack(fill=X, padx=10)

    new_submit_btn = tb.Button(register_tab, text="Submit" ,style=".TButton", command= lambda : getRegistrationData(new_username_entry.get() , new_password_entry.get() , confirm_password_entry.get()))
    new_submit_btn.pack(fill=X, padx=10 , pady=15)

    notebook.add(login_tab , text="Login")
    notebook.add(register_tab , text="Register")


    root.mainloop()
    
def main():
    user_accountsGUI()
main()







# async def bet(bet, username, one, two, three, four, play):
#   # Validate the bet.
#   try:
#     bet = int(bet)
#   except:
#     messagebox.showerror("Error", "Please enter an integer value.")
#     return

#   # Check if the user has enough money.
#   with open("accounts.txt", "r") as f:
#     for line in f:
#       user, passw, money = line.strip().split(":")
#       if user == username:
#         if bet < 1:
#           messagebox.showerror("Error!", "Bet can't be 0 or less than zero.")
#         elif bet > int(money):
#           messagebox.showerror("Error!", f"Insufficient balance. Bet can't be more than {money}$")
#         else:
#           # Place the bet.
#           symbols = await spinJackpot(one, two, three, four, play, bet)
#           gameResults(symbols, bet)
#           break

# async def spinJackpot(one, two, three, four, play, bet):
#   # Spin the reels.
#   await spin(one, 9, play)
#   await spin(two, 18, play)
#   await spin(three, 29, play)
#   await spin(four, 45, play)

#   # Get the symbols.
#   symbols = [one.cget("text"), two.cget("text"), three.cget("text"), four.cget("text")]

#   return symbols

# async def spin(label, count, play):
#   # Spin the reel.
#   for i in range(count):
#     await asyncio.sleep(0.5)
#     update_label(label)

# def gameResults(symbols, bet):
#     print(symbols , bet)
  # Determine the payout.
#   payout = 0
#   for symbol in symbols:
#     if symbol == "❤️":
#       payout += 1
#     elif symbol == "🗝️":
#       payout += 5
#     elif symbol == "💵":
#       payout += 10
#     elif symbol == "💎":
#       payout += 50

#   # Update the user's balance.
#   with open("accounts.txt", "r+") as f:
#     lines = f.readlines()
#     for i in range(len(lines)):
#       user, passw, money = lines[i].strip().split(":")
#       if user == username:
#         lines[i] = f"{user}:{passw}:{money - bet + payout}\n"
#         break

#     f.seek(0)
#     f.truncate()
#     f.writelines(lines)

#   # Show the results.
#   messagebox.showinfo("Results", f"You won {payout} dollars!")

# def getRandomSymbol():
#   symbols = ["❤️", "🗝️", "💵", "💎"]
#   return random.choice(symbols)

# def update_label(label):
#   symbol = getRandomSymbol()
#   label.config(text=symbol) 











