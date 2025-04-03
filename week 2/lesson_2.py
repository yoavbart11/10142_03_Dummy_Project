def q1():
    num = int(input("enter number: "))
    res = num%2
    print(f'The remainder of dividing {num} by 2 is {res}')

def q2():
    num = int(input("enter number: "))
    res = num%10
    print(f'The unity digit of {num} is {res}')

def q3():
    num = int(input("enter number: "))
    res = num%100
    print(f'The right 2 digits of {num} are {res}')

def q4():
    num = int(input("enter number: "))
    res = num//10
    print(f'The number {num} without the unity digit is {res}')

def q5():
    num = int(input("enter number: "))
    res = num//100
    print(f'The number {num} without the 2 right digits is {res}')

def q6():
    num = input("enter number: ")
    new_num = num.rjust(2,"0")
    print(new_num)

def q7():
    num = int(input("enter number: "))
    left_num = str((num//100)%24).rjust(2,"0")
    right_num = str((num%100)%60).rjust(2,"0")
    print(f'The time is {left_num}:{right_num}')

def q8():
    num = int(input("enter number: "))
    right_num1 = num%10
    right_num2 = (num%100)//10
    left_num1 = num//1000
    left_num2 = (num//100)%10
    res = (right_num1+right_num2) == (left_num1+left_num2)
    print(f'Does {num} meet the requirement? {res}')

def q9():
    num = int(input("enter number: "))
    right_num = num%10
    left_num = num//10
    res = (right_num or left_num) == 4
    print(f'Does {num} meet the requirement? {res}')

def q10():
    num = int(input("enter num: "))
    res1 = ((num%3) == 0)
    res2 = (num%10 == num//1000) and ((num%100)//10) == ((num//100)%10)
    print(f'Does {num} meet the req? {res1 and res2}')
    
def q11():
    num1 = float(input("enter number1: "))
    num2 = float(input("enter number2: "))
    res = (num1/num2)
    #res1 = int(num1/num2*100)/100
    print(f'The number U need is {res:.2f}')

def q12():
    num = int(input("enter number: "))
    res1 = num%2 == 0
    res2 = num < 0
    print(f'Does {num} meet the req? {res1 or res2}')

def q13():
    num = int(input("enter number: "))
    res = 10 < num < 20
    print(f'Is {num} not in the range 10-20? {not res} ')

def q14():
    word = input("type a word: ")
    res = "a" in word
    print(f'Is word {word} valid? {res}')

def q15():
    word1 = input("enter word1: ")
    word2 = input("enter word2: ")
    res1 = "a" in word1
    res2 = "a" in word2
    print(f'Does {word1} and {word2} meet the req? {res1 or res2}')
# TEMP = input("enter the temp: ")
# DEG = int(input("enter the deg: "))
def q16():
    res = (TEMP == "sunny") and (DEG < 27)
    print(f'Is it good day for picnic? {res}')

#ATE = int(input("enter ate per: "))
#DEL = int(input("enter del per: "))
#DEL5 = input("enter del5 yes or no: ")
def q17():
    res1 = ATE >= 80
    res2 = DEL >= 70
    res3 = DEL5 == "yes"
    print(f'Can student participate exam? {res1 and res2 and res3}')

#FRU = int(input("enter the number of fruits: "))
#APL_VAL = int(input("enter apple val: "))
#ORE_VAL = int(input("enter orange val: "))
def q18():
    res1 = FRU > 10
    res2 = APL_VAL == ORE_VAL
    print(f'Does customer get a discount? {res1 or res2}')

#GRE = int(input("enter student grade: "))
def q19():
    res = (GRE >= 75) and (GRE <= 90)
    print(f'Do i get discount? {res}')

#PASS_GRA = int(input("enter grade pass: "))
#COU_IN = input("did U participate in python course: ")
def q20():
    res1 = PASS_GRA > 55
    res2 = COU_IN == "no"
    print(f'Is a student eligible to enroll an OOP Java course? {res1 and res2}')

def q21():
    num = input("enter number: ")
    res = "." in num
    print(f'Does number {num} is decimal? {res}')

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
    #q15()
    #q16()
    #q17()
    #q18()
    #q19()
    #q20()
    #q21()

if __name__ == '__main__':
    main()