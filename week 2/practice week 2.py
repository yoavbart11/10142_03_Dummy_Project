def q1():
    number = int(input("enter number: "))
    year = number%10000
    month = (number//10000)%100
    day = number//1000000
    print(f'The date is {day}/{month}/{year}')

def q2():
    number = int(input("enter number: "))
    right_dig = number%10
    middle_dig = (number//10)%10
    left_dig = number//100
    res = right_dig >= 2*(middle_dig+left_dig)
    print(res)

def q3():
    number = int(input("enter number: "))
    right_num = number%10
    left_num = number//1000
    middle_num1 = (number%100)//10
    middle_num2 = (number//100)%10
    res = (left_num +1 == right_num) and (middle_num1 == middle_num2)
    print(res)

def q4():
    x = 5
    x = 6
    print(x)


def main():

    #q1()
    #q2()
    #q3()
    q4()

if __name__ == '__main__':
    main()