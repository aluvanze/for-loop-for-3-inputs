for i in range(1):
    y = int(input("input english\n"))
    z = int(input("input kiswahili\n"))
    x = int(input("input math\n"))
    sum=x+y+z
    average=(x+y+z)/3
    while average > 8:
        print("Good Work")

        break
    else:
        print("try harder next time")

    print("Sum",sum)
    print("average", average)
