import prompt

def run_game(game_module):
    """
    Запускает игру.
    game_module должен содержать:
    - DESCRIPTION: str
    - generate_round() -> (question: str, correct_answer: str)
    """
    print("Welcome to the VD Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_module.DESCRIPTION)

    for _ in range(3):
        question, correct = game_module.generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
