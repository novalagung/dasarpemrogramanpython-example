print("from myprogram.py:", __name__)

import calculate

import random
num = random.randint(0, 999)
calculate.is_prime(num)
