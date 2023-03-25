# Discord bot commands
import random
import discord
import responses


async def send_message(message, user_message, is_private):
    try:  # Try to send a message
        response = responses.get_response(user_message)  # Get the response from the user's message

        # Send the response to the user
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


ranks = {
    'F': 0,
    'D': 1,
    'C': 3,
    'B': 4,
    'A': 10,
    'S': 15,
}

users = {
    'Dark#6189': {
        'rank': 'F',
        'wins': 0
    },
    'user2': {
        'rank': 'F',
        'wins': 0
    },
}


def run_discord_bot():
    TOKEN = ''
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} sent a message in {channel}: {user_message}')

        if user_message[0] == '?':  # If the message starts with a question mark
            user_message = user_message[1:]  # "?Help" -> "Help", i.e., ignores the question mark
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

        # Check Rank
        if user_message == '!rank':
            await message.channel.send(f'Your rank is {users[username]["rank"]}')

        # Check Wins
        if user_message == '!wins':
            await message.channel.send(f'You have {users[username]["wins"]} wins')

        # RPG stuff
        if message.content.startswith('!fight'):
            username = str(message.author)

            # If the user is new, initialize their rank to F and wins to 0
            if username not in users:
                users[username] = {
                    'rank': 'F',
                    'wins': 0
                }

            player_hp = 100
            enemy_hp = 10
            player_attack = 10
            enemy_attack = 10

            # Store the previous rank before the fight
            previous_rank = users[username]['rank']

            while True:
                # player's turn
                player_damage = random.randint(1, player_attack)
                enemy_hp -= player_damage
                await message.channel.send(f'You hit the enemy for {player_damage} damage!')
                if enemy_hp <= 0:
                    await message.channel.send('You win!')
                    users[username]['wins'] += 1

                    # Check if the user qualifies for a promotion
                    for rank in sorted(ranks, key=ranks.get, reverse=True):
                        if users[username]['wins'] >= ranks[rank]:
                            if rank != users[username]['rank']:
                                users[username]['rank'] = rank
                                await message.channel.send(
                                    f'Congratulations, {username}! You have been promoted to rank {rank}!')
                            break

                    break

                # enemy's turn
                enemy_damage = random.randint(1, enemy_attack)
                player_hp -= enemy_damage
                await message.channel.send(f'The enemy hit you for {enemy_damage} damage!')
                if player_hp <= 0:
                    await message.channel.send('You lose!')
                    break

            # Update the previous rank for the user
            users[username]['previous_rank'] = previous_rank

    client.run(TOKEN)
