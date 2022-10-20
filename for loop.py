subjects=3

for i in range(subjects):


    x = int(input("input english\n"))

    i=i+1

    if i==1:
        y = int(input("input math\n"))
    i=i+1

    if i==2:
            z = int(input("input kiswahili\n"))
            i=i+1

    if i == 3:
        a = int(input("input sheng\n"))
        i=0+1





    sum = x + y + z + a
    average = (x + y + z + a) / 4
    while average > 8:
        print("Good Work")

        break
    else:
        print("try harder next time")

    print("Sum", sum)
    print("average", average)
