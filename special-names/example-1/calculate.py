print("from calculate.py:", __name__)

def is_prime(num):
    print("from calculate.py is_prime(num):", __name__)

    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
