def is_prime(num):
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

if __name__ == '__main__':
    num_test = 104
    print("testing is_prime() func")
    is_prime(num_test)
