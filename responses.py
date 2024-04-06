from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
            return "Speak up!"
    elif 'hello' in lowered:
            print('Got hello')
            return "Hi!"
    elif 'bye' in lowered:
            print('Got bye')
            return "See ya"
    elif 'roll dice' in lowered:
            print('Got roll dice')
            return f'You rolled: {randint(1, 6)}'
    else:
            print('Got no match')
            return choice(['Huh?',
                           'What?',
                           '??'])