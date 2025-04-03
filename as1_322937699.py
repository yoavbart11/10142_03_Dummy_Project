# Q1
def q1():
    print('Q1')
    num1 = int(input("enter number1: "))
    num2 = int(input("enter number2: "))
    num3 = int(input("enter number3: "))
    if (num2 < num1 < num3) or (num3 < num1 < num2):
        print(f'The middle number is {num1}')
    elif (num1 < num2 < num3) or (num3 < num2 < num1):
        print(f'The middle number is {num2}')
    elif (num1 < num3 < num3) or (num2 < num3 < num1):
        print(f'The middle number is {num3}')

# Q2
def q2():
    print('Q2')
    num = int(input("enter number: "))
    dig1 = num%10
    dig2 = (num%100)//10
    dig3 = (num%1000)//100
    if (dig1 > dig2) and (dig1 > dig3):
        print(f'The largest digit is {dig1}')
    elif (dig2 > dig1) and (dig2 > dig3):
        print(f'The largest digit is {dig2}')
    else:
        print(f'The largest digit is {dig3}')

# Q3
def q3():
    print('Q3')
    side1 = float(input("enter side1: "))
    side2 = float(input("enter side2: "))
    side3 = float(input("enter side3: "))
    if (side1 == side2) or (side2 == side3) or (side1 == side3):
        if side1 == side2 == side3:
            print("The triangle is equilateral")
        else:
            print("The triangle is isosceles")
    else:
        if ((side1 + side2) < side3) or ((side1 + side3) < side2) or ((side2 + side3) < side1):
            print("Invalid triangle")
        else:
            print("The triangle is scalene")

# Q4
def q4():
    print('Q4')
    time = int(input("enter number: "))
    if time == 0:
        print(f'The time in 12-Hour format:{12}AM')
    elif ((time//12) > 0) and ((time%12) == 0):
        print(f'The time in 12-Hour format:{12}PM')
    elif (time//12)%2 != 0:
        print(f'The time in 12-Hour format:{time%12}PM')
    elif (time//12)%2 == 0:
        print(f'The time in 12-Hour format:{time%12}AM')

def q5():
    print('Q5')
    pre_present = int(input("enter the present in class percent: "))
    final_exam_gra = int(input("enter the final exam grade: "))
    middle_exam_gra = int(input("enter the middle exam grade: "))
    homework_gra = int(input("enter homework grade: "))
    res1 = (final_exam_gra*0.9) + (homework_gra*0.1)
    res2 = (final_exam_gra*0.7) + (middle_exam_gra*0.2) + (homework_gra*0.1)
    if pre_present < 80:
        print("Your final mark is 0")
    else:
        if final_exam_gra < 60:
            print(f'Your final mark is {final_exam_gra}')
        else:
            if middle_exam_gra < final_exam_gra:
                print(f'Your final mark is {res1}')
            else:
                if middle_exam_gra > final_exam_gra:
                    print(f'Your final mark is {res2}')

def main():
    #q1()
    #q2()
    q3()
    #q4()
    #q5()

if __name__ == '__main__':
    main()