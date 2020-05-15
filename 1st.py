maximum = int(input("Please Enter any Maximum Value : "))

if (maximum==1):
    print("1")
else:
    for number in range(0, (maximum*2)+2):
        if(number % 2 != 0 and number % 5 != 0):
            print(number, end=',')
