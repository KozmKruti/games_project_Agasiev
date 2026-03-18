import random
import math

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def generate_round():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    correct = math.gcd(a, b)
    question = f"{a} {b}"
    return question, str(correct)
