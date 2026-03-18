import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_round():
    number = random.randint(1, 50)
    correct = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return question, correct
