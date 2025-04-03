from math import pi
def q1():
    my_name = input("please enter your name: ")
    print(f'your name is {my_name}')

def q2():
    age = int(input("please type your age: "))
    print(f'your age is {age}, in five years your age will be {age+5}')

PI = 3.14
def q3():
    radius = float(input("enter radius: "))
    area = PI * radius ** 2
    perimeter = 2 * pi * radius
    print(f'radius = {radius}, area = {area}, perimeter = {perimeter}')

def q4():
    length = int(input("enter length: "))
    width = int(input("enter width: "))
    area = length * width
    perimeter = (length*2) + (width*2)
    print(f'length = {length}, width = {width}, area = {area}, perimeter = {perimeter}')

def q5():
    ch = input("enter ch: ")
    print(f'{ch}\n{ch}\n{ch}')

def q6():
    ch = input("enter ch: ")
    print(f'{ch} {ch}')
    print(ch, end=" ")
    print(ch, end=" ")
    print(ch)

def q7():
    ch = input("enter ch: ")
    print(f'{ch} is located in {ord(ch)} row')

def q8():
    tav = int(input("enter num: "))
    print(f'{tav} is represent \'{chr(tav)}\'')

def q9():
    ch = input("enter ch: ")
    print(f'The lower letter for {ch} is {chr(ord(ch)+32)}')

def q10():
    ch = input("enter ch: ")
    print(f'The real character for {ch} is {(chr(ord(ch)-3))}')

def q11():
    word = input("enter word: ")
    print(f'The represent print for Python is {word.rjust(10,"*")}')

def q12():
    num_word = input("enter num: ")
    print(f'The represent print for {num_word} is {num_word.rjust(4,"0")}')

START_PR = 15.2
PR_KM = 1.9
CASE_PR = 7
def q13():
    km_drove = float(input("enter km: "))
    case_num = int(input("enter case: "))
    print(f'distance = {km_drove},'
          f'amount_of_suitcase = {case_num},'
          f'price = {(PR_KM*km_drove) + (case_num*CASE_PR) + START_PR}')

STOP_FL = 5
PAS_TM = 3
def q14():
    elv_floor = int(input("enter elv floor: "))
    start_floor = int(input("enter start floor: "))
    target_floor = int(input("enter floor U need: "))
    total_time = (PAS_TM*abs(elv_floor-start_floor)+(PAS_TM*abs(target_floor-start_floor)) + STOP_FL*2)
    print(f'The total time is {total_time} seconds')

def q15():
    width = int(input("enter width: "))
    length = int(input("enter length: "))
    width, length = length, width
    print(f'length = {length}, width = {width}')

def main():
    #q1()
    #q2()
    #q3()
    #q4()
    #q5()
    #q6()
    #q7()
    #q8()
    #q9()
    #q10()
    #q11()
    #q12()
    #q13()
    #q14()
    q15()

if __name__ == '__main__':
    main()