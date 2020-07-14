import random as rd
import time


def oddoreven(num, mnum):
    if (num+mnum) % 2 == 0:
        print("Even")
        o = 'E'
    else:
        print("Odd")
        o = 'O'
    return o


def validation_bat(bat):
    if bat > 6 or bat < 0:
        print("No Ball")
        run_player = 0


def validation_bowl(bowl):
    if bowl > 6 or bowl < 0:
        print("Wide")
        run_mac += 1


def batting():
    print(end="\t\t""Batting")
    print(end="\n")
    run_player = 0
    for i in range(0, 6):
        mac = rd.randint(1, 6)
        bat = int(input(f"Bat[{i+1}] :"))
        validation_bat(bat)
        time.sleep(1.0)
        if bat == mac:
            print("Out!")
            print("Total Run =", run_player)
            break
        else:
            run_player = run_player+bat
            print("Run =", run_player)
    return run_player


def bowling():
    print(end="\t\t""Bowling")
    print(end="\n")
    run_mac = 0
    for i in range(0, 6):
        mac = rd.randint(1, 6)
        bowl = int(input(f"Bowl[{i+1}] :"))
        validation_bowl(bowl)
        time.sleep(1.0)
        if bowl == mac:
            print("Out!")
            print("Total Run =", run_mac)
            break
        else:
            run_mac = run_mac+mac
            print("Run =", run_mac)
    return run_mac


def result():
    if a > b:
        print("You Win!")
    elif b > a:
        print("You Lose")
    else:
        print("Its a Draw!")


# main
print(end="\t\t""Cricket")

# Odd Or Even_1
print(end="\n")
odd_even = input("[O]dd Or [E]ven: ")
if odd_even.upper() == 'O':
    print("You Chose Odd")
elif odd_even.upper() == 'E':
    print("You Chose Even")
else:
    print("Wrong Entry")
    exit()

# Odd Or Ever
num = int(input("Enter Your Number: "))
mnum = rd.randint(1, 2)
time.sleep(1.0)
print("Computer Chose:", mnum)
print("Total:", num+mnum)
retval = oddoreven(num, mnum)

# if player wins toss
if retval == odd_even.upper():
    print(end="\n""1.Bowl")
    print(end="\n""2.Bat")
    print(end="\n""0.Exit")
    print(end="\n")
    ch = int(input("Enter Your Choice < 1/2 >"))
    if ch == 1:
        b = bowling()
        time.sleep(0.5)
        a = batting()
        result()
    elif ch == 2:
        a = batting()
        time.sleep(0.5)
        b = bowling()
        result()
    elif ch == 0:
        print("Exiting...")
        time.sleep(1.0)
        exit()
    else:
        print("Invalid")
else:
    print("Coming Soon!")
