MIN_TEMP =11
def q1():
    temp = int(input("enter temp: "))
    if temp < MIN_TEMP:
        print("It's going to be a cold day")
    else:
        print("The temp is over 11 temp")

MIN_AGE = 18
def q2():
    age = int(input("enter the age: "))
    if age > MIN_AGE:
        print("You are adult")
    else:
        print("You are still young")

CLOUD_STATUS = "yes"
def q3():
    cloud = input("enter if there are clouds: ")
    temp = int(input("enter the temp: "))
    if cloud == CLOUD_STATUS and temp < MIN_TEMP:
        print("It's going to rain")

def q4():
    java_grade = int(input("enter java grade: "))
    python_grade = int(input("enter python grade: "))
    if (java_grade > 60) and (python_grade > 60):
        print("Registration fot OOP course confirmed")
    else:
        print("end program")

def q5():
    java_grade = int(input("enter java grade: "))
    python_grade = int(input("enter python grade: "))
    if (java_grade > 60) or (python_grade > 60):
        print("Registration fot OOP course confirmed")
    else:
        print("end program")

def q6():
    cloud = input("enter if there are clouds: ")
    temp = int(input("enter the temp: "))
    if cloud == CLOUD_STATUS and temp < MIN_TEMP:
        print("It's going to rain")
    else:
        print("It's not going to rain")

def q7():
    num = int(input("enter number: "))
    res1 = num%2 == 0
    dig1 = num%10
    dig2 = (num//10)%10
    dig3 = num//100
    res2 = ((dig1 == 3) or (dig2 == 3) or (dig3 == 3))
    if res1 and res2:
        print("The number meets the req")
    else:
        print("The number does not meet...")

def q8():
    side1 = int(input("enter side1: "))
    side2 = int(input("enter side2: "))
    side3 = int(input("enter side3: "))
    if ((side1 + side2) > side3) and ((side1 + side3) > side2) and ((side2 + side3) > side1):
        print("OK")
    else:
        print("Wrong")

def q9():
    num = int(input("enter num: "))
    if (num >= 10) and num < 100:
        print(f'{num} is 2 dig num')
    elif (num >= 1000) and num < 10000:
        print(f'{num} is 4 dig num')
    else:
        print("num is not 2 dig or 4 dig num")

def q10():
    grade = int(input("enter your grade: "))
    if grade > 90:
        res = "Great!"
    elif grade > 80:
        res = "Good!"
    elif grade >= 60:
        res = "Pass!"
        if grade < 70:
            res += "\nPractice more!"
    else:
        res = "Fail!"
    print(res)

def q11():
    num1 = float(input("enter num1: "))
    num2 = float(input("enter num2: "))
    action = input("enter action: ")
    res1 = num1 + num2
    res2 = num1 - num2
    res3 = num1 * num2
    text = "Invalid Operation"
    if action == "+":
        text = res1
    elif action == "-":
        text = res2
    elif action == "*":
        text = res3
    print(text)

LOW_PRICE = 120
MID_PRICE = 150
HIGH_PRICE = 180
VERY_HIGH_PRICE = 200
def q12():
    room_num = int(input("enter room number apartment: "))
    price = 120
    if room_num == 5:
        size = input("enter regular/better: ")
        if size == "regular":
            price = HIGH_PRICE
        elif size == "better":
            price = VERY_HIGH_PRICE
    elif room_num == 3:
        price = LOW_PRICE
    else:
        price = MID_PRICE
    print(f'The amount to be paid is {price} NIS')

def q13():
    number = int(input("enter number: "))
    res = number%2 == 0
    val_dig = "even number" if res else "odd number"
    print(f"Your number is {val_dig}")

def q14():
    number = float(input("enter number: "))
    val_num = "in range" if 10 < number <= 20 else "out of range"
    print(f'{number} is {val_num}')

def q15():
    number = int(input("enter number: "))
    val_num = "positive num" if number > 0 else "zero number" if number == 0 else "negative num"
    print(f'{number} is {val_num}')

def q16():
    number = int(input("enter number: "))
    res = "Good Year"
    res1 = number%4 == 0
    res2 = number%100 == 0
    res3 = number%400 == 0
    if res3 or (res1 and not res2):
        res = "Good Year"
    else:
        res = "False Year"
    print(res)

DAY_1 = 28
DAY_2 = 29
DAY_3 = 30
DAY_4 = 31
def q17():
    month = input("enter month: ")
    year = int(input("enter if itws Good Year: "))
    month1 = ("january", "march", "july", "may", "august", "october", "december")
    month2 = ("april", "june", "september", "november")
    res = 0
    res1 = year % 4 == 0
    res2 = year % 100 == 0
    res3 = year % 400 == 0
    if month in month1:
        res = DAY_4
    elif month in month2:
        res = DAY_3
    elif month == "February":
        if res3 or (res1 and not res2):
            res = DAY_2
        else:
            res = DAY_1
    print(res)

def q18():

def q19():

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
    q17()

if __name__ == '__main__':
    main()