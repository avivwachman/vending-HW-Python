""" Vending Machine,   Aviv Wachman"""
import sys


def init_machine():
    num_mach = {
        "1": "Ness Coffee",
        "2": "Coffee Black",
        "3": "Tea",
        "4": "Hot Chocolate",
        "5": "Soup",
        "6": "Coca-Cola",
        "7": "Orange Juice"
    }
    money_mach = (2.4, 2.1, 1.6, 2.5, 3.1, 3.3, 3.2)
    return num_mach, money_mach


def print_menu(num_mach, money_mach):
    print("""         MENU\n        ~~~~~~""")
    for bev_num in num_mach:
        beverage_name = num_mach[bev_num]
        print(bev_num + ".   ", beverage_name, money_mach[int(bev_num) - 1])
    print()


def choose(num_mach, money_mach):
    bev = input("Choose by number -->")
    print(f"You chose {num_mach[bev]}")
    nis_to_get = money_mach[int(bev) - 1]
    print(f"Enter {nis_to_get} NIS -->", end='')
    return nis_to_get


def enough_nis():
    print("Thank you for using my beverage machine")
    sys.exit()


def print_coins(excess):
    coins = (20, 10, 5, 2, 1, 0.5, 0.1)
    for coin in coins:
        if coin < excess:
            num_of_coins = int(excess / coin)
            print(num_of_coins, "coins of", coin)
            excess = excess - num_of_coins * coin + 0.0000001
    enough_nis()


def give_back(nis_to_get):
    nis_entered = input()
    excess = round(float(nis_entered) - float(nis_to_get), 2)
    if excess == 0:
        enough_nis()
    if excess < 0:
        print("Not Enough Money")
        sys.exit()
    print("Your excess is:", excess)
    return excess


if __name__ == '__main__':
    NUM_mach, MONEY_mach = init_machine()
    print_menu(NUM_mach, MONEY_mach)
    NIS_to_get = choose(NUM_mach, MONEY_mach)
    EXCESS = give_back(NIS_to_get)
    print_coins(EXCESS)
