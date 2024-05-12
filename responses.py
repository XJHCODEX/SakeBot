# functionality of how the chat-bot will respond
from random import choice, randint

def get_response(user_input: str) -> str:
    # - CHANGE LOGIC - w/ AI or response algorithm
    lowered: str = user_input.lower()
    # if an empty string is returned
    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you SakeBot' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    # if you type in "roll dice", the bot will roll a dice.
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    # choice will choose a random response from the list when user types something the bot doesn't understand
    else:
        return choice(['I dont not understand...',
                        'Could you clarify?...',
                        'Do you mind rephrasing that?',])
    # - CHANGE LOGIC - 