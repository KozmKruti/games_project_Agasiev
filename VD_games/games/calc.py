import random

DESCRIPTION = 'What is the result of the expression?'

def generate_round():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    op = random.choice(['+', '-', '*'])

    if op == '+':
        correct = a + b
    elif op == '-':
        correct = a - b
    else:
        correct = a * b

    question = f"{a} {op} {b}"
    return question, str(correct)
