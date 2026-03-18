import random

DESCRIPTION = 'What number is missing in the progression?'

def generate_round():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    hidden_index = random.randint(0, length - 1)

    progression = []
    for i in range(length):
        value = start + i * step
        progression.append(str(value))

    correct = progression[hidden_index]
    progression[hidden_index] = '..'

    question = ' '.join(progression)
    return question, correct
