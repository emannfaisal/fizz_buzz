print("------Fizz Buzz------")
target = int(input("What is your target number? "))
for number in range(1,target+1):
    if number%3 == 0 and number%5 ==0:
        print("FizzBUzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("BUzz")
    else:
        print(number)