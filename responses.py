import random


def get_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return """```Available commands:
        !fight - to begin the battle!
        !rank - to check your current rank
        !win - to see how many wins you have
        !stat - your current status
        MORE TO COME!!!```"""  # This is a Markdown code block
    

    
