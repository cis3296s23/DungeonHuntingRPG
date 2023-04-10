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
        !shop - to buy items!
        !inventory - to see your inventory!
        !stat - to see your stats!
        MORE TO COME!!!```"""  # This is a Markdown code block
    

    
