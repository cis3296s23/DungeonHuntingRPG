import random


def get_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hello!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`Available commands: hello, roll.`"  # This is a Markdown code block
    
    if p_message == 'test':
        return 'test completed'
    
    if p_message == 'test2':
        return 'Here is test2!'
