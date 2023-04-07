# Discord bot commands
import random
import discord
import responses

CHANNEL_ID = 1075850854126583900
BOT_TOKEN = 'enter token here'  # remove before committing


async def send_message(message, user_message, is_private):
    try:  # Try to send a message
        response = responses.get_response(user_message)  # Get the response from the user's message

        # Send the response to the user
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


ranks = {
    'F': {'wins_required': 0, 'enemy': 'Centipede'},
    'D': {'wins_required': 1, 'enemy': 'Stone Golem'},
    'C': {'wins_required': 3, 'enemy': 'Knight'},
    'B': {'wins_required': 4, 'enemy': 'Insect Queen'},
    'A': {'wins_required': 10, 'enemy': 'Ant King'},
    'S': {'wins_required': 15, 'enemy': 'Kamish'},
}

enemies = {
    'Centipede': {'hp': 10, 'atk': 10,
                  'img': "https://static.wikia.nocookie.net/solo-leveling/images/e/e8/Centipede1.jpg/revision/latest/scale-to-width-down/350?cb=20210628033630"},
    'Stone Golem': {'hp': 20, 'atk': 20,
                    'img': "https://static.wikia.nocookie.net/solo-leveling/images/4/47/StoneGolem1.jpg/revision/latest/scale-to-width-down/350?cb=20210628163114"},
    'Knight': {'hp': 30, 'atk': 30,
               'img': "https://static.wikia.nocookie.net/solo-leveling/images/b/bd/Igris13.jpg/revision/latest/scale-to-width-down/350?cb=20210901144428"},
    'Insect Queen': {'hp': 40, 'atk': 40,
                     'img': "https://static.wikia.nocookie.net/solo-leveling/images/f/fe/Querehsha1.jpg/revision/latest/scale-to-width-down/350?cb=20210803223313"},
    'Ant King': {'hp': 50, 'atk': 50,
                 'img': "https://static.wikia.nocookie.net/solo-leveling/images/9/93/Beru_%28Marshal%29.jpg/revision/latest/scale-to-width-down/343?cb=20210727041130"},
    'Kamish': {'hp': 60, 'atk': 60,
               'img': "https://static.wikia.nocookie.net/solo-leveling/images/7/72/Kamish2.jpg/revision/latest/scale-to-width-down/350?cb=20210406203322"},
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
    TOKEN = BOT_TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        channel = client.get_channel(CHANNEL_ID)

        await channel.send(
            "Welcome to the Dungeon Hunting RPG! The Dungeon Hunting RPG sets up enemies for the players to fight, dungeons to explore, checking of current adventure guild rank, displaying their health bars, and more. The players interact with the bot with commands to decide what actions they want to take.\n")
        await channel.send(
            'To start your adventure, enter \'!fight\'.\nEnter \'!help\' for the list of actions you can take.\n')

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
            embed = discord.Embed(title="Rank", description=f'Your rank is {users[username]["rank"]}', color=0x00ff00)
            await message.channel.send(embed=embed)

        # Check stats
        if user_message == '!stat':
            embed = discord.Embed(colour=discord.Color.from_rgb(247, 38, 42), title=username + '\'s stats\n',
                                  description=f'Rank: {users[username]["rank"]}\n' +
                                              f'Wins: {users[username]["wins"]}\n')
            await message.channel.send(embed=embed)

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

            rank = users[username]['rank']

            # Check if the user has reached the required number of wins for their rank
            if users[username]['wins'] >= ranks[rank]['wins_required']:
                enemy_name = ranks[rank]['enemy']
            else:
                # If the user hasn't reached the required number of wins, they fight their previous enemy
                enemy_name = enemies[users[username]['previous_enemy']]['name']

            enemy = enemies[enemy_name]
            enemy_hp = enemy['hp']
            enemy_atk = enemy['atk']
            enemy_img = enemy['img']
            users[username]['previous_enemy'] = enemy_name

            player_hp = 100
            player_atk = 10

            # Store the previous rank before the fight
            previous_rank = users[username]['rank']

            # Create an embed to display the fight
            embed = discord.Embed(title="Challenging Dungeon! :crossed_swords:", color=0x00FF9900)
            embed.add_field(name=f"{username} HP :heart:", value=player_hp, inline=True)
            embed.add_field(name=f"{enemy_name} HP :space_invader:", value=enemy_hp, inline=True)
            embed.set_image(url=enemy_img)

            # Send the embed
            fight_message = await message.channel.send(embed=embed)

            while True:
                # player's turn
                player_damage = random.randint(1, player_atk)
                enemy_hp -= player_damage

                # Update the embed
                embed.set_field_at(0, name=f"{enemy_name} HP :space_invader:", value=f"{enemy_hp}/100", inline=False)
                embed.description = f'You dealt {player_damage} damage to the enemy!'

                await fight_message.edit(embed=embed)

                if enemy_hp <= 0:
                    await message.channel.send('You win!')
                    users[username]['wins'] += 1

                    # Check if the user qualifies for a promotion
                    for rank in sorted(ranks, key=lambda x: ranks[x]['wins_required'], reverse=True):
                        if users[username]['wins'] >= ranks[rank]['wins_required']:
                            if rank != users[username]['rank']:
                                users[username]['rank'] = rank
                                await message.channel.send(
                                    f'Congratulations, {username}! You have been promoted to rank {rank}!')
                            break
                    break
                # enemy's turn
                enemy_damage = random.randint(1, enemy_atk)
                player_hp -= enemy_damage

                # Update the embed
                embed.set_field_at(1, name=f"{username} HP :heart:", value=f"{player_hp}/100", inline=False)
                embed.description = f'The enemy dealt {enemy_damage} damage to you!'
                await fight_message.edit(embed=embed)

                if player_hp <= 0:
                    await message.channel.send('You lose!')
                    break

            # Update the previous rank for the user
            users[username]['previous_rank'] = previous_rank

    client.run(TOKEN)
