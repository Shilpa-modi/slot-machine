import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROW=3
COL=3

sym_count={
   "A":2,
   "B":4,
   "C":6,
   "D":8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def slot(row,col,sym):
    all_sym=[]
    for sym,sym_count in sym.items():
      for _ in range(sym_count):
         all_sym.append(sym)

    column=[]
    for _ in range(col):
        current_sym=all_sym[:]
        columns=[]
        
        for _ in range(row):
            value=random.choice(current_sym)
            current_sym.remove(value)
            columns.append(value)
        column.append(columns)
         
    return column   

def print_slot(column):
    for row in range(len(column[0])):
        for i,columns in enumerate(column):
            if i !=len(column)-1:
                print(columns[row],end=" | ")
            else:
                print(columns[row],end=" ")

        print()


def deposit():
    while True:
        amount=input("enter deposit:")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
               break
            else:
              input("enter no. greater than 0")
        else:    
           input("enter a no.")
    return amount

def lines_no():
    while True:
        lines=input("enter lines (1-" + str(MAX_LINES) +")")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<= MAX_LINES:
               break
            else:
              input("enter line in the range:")
        else:    
           input("enter a no.:")
    return lines

def get_bet():
    while True:
        bet=input(f"enter bet amount between {MAX_BET} and {MIN_BET}:")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<=bet<=MAX_BET:
               break
            else:
              input(f"enter valid amount between {MAX_BET} and {MIN_BET}:")
        else:    
           input("enter a no.")
    return bet

def check_winnings(column,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=column[0][line]
        win=True
        for col in column:
            if col[line]!=symbol:
                win=False
                break
        if win:
                winnings+=values[symbol]*bet
                winning_lines.append(line+1)
    return winnings,winning_lines

def spin(balance):
    lines=lines_no()
    while True:
        bet=get_bet()
        total_bet=bet*lines

        if total_bet>balance:
            print(f"not enough money,your balance is ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines.Total bet is ${total_bet}")
    slots=slot(ROW,COL,sym_count)
    print_slot(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
    if winning_lines:
        print(f"You won on lines:", *winning_lines)
    else:
        print("no winning lines")
    return winnings - total_bet

def main():
    balance=deposit()
    while True:
        print(f"Current balance ${balance}")
        answer=input("press enter to play or press q to quit")
        if answer=="q":
            break
        balance+=spin(balance)
    print(f"you left with ${balance}")

main()