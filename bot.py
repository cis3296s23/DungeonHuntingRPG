# Discord bot commands
import random
import discord
import shop

CHANNEL_ID = 1075850854126583900
BOT_TOKEN = 'enter token here'  # remove before committing

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
        'wins': 0,
        'gold': 0,  # gold gained from fighting monsters
        'inventory': {},  # inventory to store items from shop
        'weapon_equip': 'No weapons equipped',
        'armor_equip': 'No armor equipped',
        'health': 100
    },
    'user2': {
        'rank': 'F',
        'wins': 0,
        'gold': 0,
        'inventory': {},
        'weapon_equip': 'No weapons equipped',
        'armor_equip': 'No armor equipped',
        'health': 100
    },
}

shop_items = {  # shop, displays items and the amount of gold for them
    'dull sword': 10,
    'shape sword': 40,
    'great sword': 100,
    'light armor': 20,
    'medium armor': 50,
    'heavy armor': 100,
    'health potion': 10
}

weapon_dmg = {  # added damage when equipped
    'dull sword': 10,
    'shape sword': 20,
    'great sword': 40,
}

armor_health = {  # added health when equipped
    'light armor': 10,
    'medium armor': 20,
    'heavy armor': 40,
}

welcome_message = 'Welcome to the Dungeon Hunting RPG! The Dungeon Hunting RPG sets up enemies for the players to ' \
                  'fight, dungeons to explore, checking of current adventure guild rank, displaying their health ' \
                  'bars, and more. The players interact with the bot with commands to decide what actions they want ' \
                  'to take.\n'
welcome_message2 = 'To start your adventure, enter \'**!fight**\'.\nEnter \'**!help**\' for the list of actions you can take.\n'


def run_discord_bot():
    TOKEN = BOT_TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        channel = client.get_channel(CHANNEL_ID)
        # send welcome message as embed
        embed = discord.Embed(title="Welcome to the Dungeon Hunting RPG!", description=welcome_message, color=0x3D85C6)
        embed.add_field(name="How to Play", value=welcome_message2, inline=False)
        embed.set_footer(text="Be sure to enjoy!")
        embed.set_thumbnail(
            url="https://static.wikia.nocookie.net/solo-leveling/images/f/f7/RedGate1.jpg/revision/latest/scale-to-width-down/350?cb=20210626163402")
        await channel.send(embed=embed)

    @client.event
    async def on_message(message):

        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} sent a message in {channel}: {user_message}')

        if username not in users:
            users[username] = {
                'rank': 'F',
                'wins': 0,
                'gold': 0,
                'inventory': {},
                'weapon_equip': 'No weapons equipped',
                'armor_equip': 'No armor equipped',
                'health': 100
            }

        # Check help command
        if user_message == '!help':
            embed = discord.Embed(title="Bot Commands", description="List of commands", color=0x3D85C6)
            embed.add_field(name="!fight", value="Fight a monster", inline=False)
            embed.add_field(name="!stat", value="Check your stats", inline=False)
            embed.add_field(name="!inventory", value="Check your inventory", inline=False)
            embed.add_field(name="!shop", value="Check the shop", inline=False)
            embed.add_field(name="!help", value="List of commands", inline=False)
            embed.add_field(name="!lb", value="Check the leaderboard", inline=False)
            embed.set_footer(text="Be sure to enjoy!")
            embed.set_thumbnail(
                url="https://static.wikia.nocookie.net/solo-leveling/images/3/3f/KillTheEnemies.jpg/revision/latest/scale-to-width-down/350?cb=20210815152958")
            await message.channel.send(embed=embed)

        # Check stats
        if user_message == '!stat':
            embed = discord.Embed(colour=discord.Color.from_rgb(247, 38, 42), title=username + '\'s stats\n',
                                  description=f'Rank: {users[username]["rank"]}\n' +
                                              f'Wins: {users[username]["wins"]}\n' +
                                              f'Gold: {users[username]["gold"]}\n' +
                                              f'Health: {users[username]["health"]}\n'
                                              f'Weapon: {users[username]["weapon_equip"]}\n' +
                                              f'Armor: {users[username]["armor_equip"]}\n')

            await message.channel.send(embed=embed)

        if user_message == '!shop':  # opens shop menu
            await message.channel.send(
                "Welcome to the shop!\nSwords increase your damage output, armors help reduce enemy damage, and health potions restore your health.\n")
            await message.channel.send("Please enter the number of the item you wish to purchase.\n")
            await message.channel.send(shop.shop_message(shop_items))  # lists shop items

        # Buy and store item into player's inventory
        if user_message == '1' or user_message == '2' or user_message == '3' or user_message == '4' or user_message == '5' or user_message == '6' or user_message == '7':

            temp = user_message
            num = int(temp) - 1
            item = list(shop_items)

            if users[username]["gold"] >= shop_items[item[num]]:  # checks if player have enough gold
                if item[num] not in users[username]['inventory']:
                    users[username]['inventory'][item[num]] = 1  # add shop item into player inventory
                else:
                    users[username]['inventory'][item[num]] += 1

                users[username]["gold"] -= shop_items[item[num]]  # take gold from player

                await message.channel.send(item[num] + ' obtained!\n')
            else:
                await message.channel.send('Not enought gold!\n')

        if user_message == '!inventory':  # open user's inventory
            if bool(users[username]["inventory"]) != False:  # check if inventory is full
                await message.channel.send('Weapon equipped: ' + users[username]['weapon_equip'] + '.\n')
                await message.channel.send('Armor equipped: ' + users[username]['armor_equip'] + '.\n')
                for x, y in users[username]["inventory"].items():
                    if x == 'health potion':
                        await message.channel.send('-' + x + ': ' + str(y))
                    else:
                        await message.channel.send('-' + x)
                await message.channel.send('Enter the name of the item you want to equip or use.\n')

            else:
                await message.channel.send(
                    'Empty inventory. You can visit the shop to purchase items by using the \'!shop\' command.\n')

        for player_item in shop_items:
            if user_message == player_item:
                if player_item in users[username]['inventory']:  # check if in inventory
                    if ("health potion" in player_item) == True:  # if it is a sword
                        if users[username]['inventory']['health potion'] >= 1:
                            await message.channel.send('Potion used, +10 health.\n')
                            users[username]['inventory'][player_item] -= 1
                            users[username]['health'] += 10
                        else:
                            await message.channel.send(
                                'No potions left in inventory, please visit the shop for more.\n')
                    else:
                        if ("sword" in player_item) == True:  # if it is a sword
                            users[username]['weapon_equip'] = player_item
                        elif ("armor" in player_item) == True:  # if it is an armor
                            users[username]['armor_equip'] = player_item
                        await message.channel.send(player_item + ' equipped!\n')

        # RPG stuff
        if message.content.startswith('!fight'):
            username = str(message.author)

            # If the user is new, initialize their rank to F and wins to 0
            if username not in users:
                users[username] = {
                    'rank': 'F',
                    'wins': 0,
                    'gold': 0,
                    'inventory': {},
                    'weapon_equip': 'No weapons equipped',
                    'armor_equip': 'No armor equipped',
                    'health': 100
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

            # player_hp = 100

            player_atk = 10

            for add_dmg in weapon_dmg:  # add additional player dmg if weapon is equipped
                if users[username]['weapon_equip'] == add_dmg:
                    player_atk += weapon_dmg[add_dmg]

            for add_health in armor_health:  # add additional player dmg if weapon is equipped
                if users[username]['armor_equip'] == add_health:
                    # player_hp += armor_health[add_health]
                    users[username]['health'] += armor_health[add_health]

            player_hp = users[username]['health']

            # Store the previous rank before the fight
            previous_rank = users[username]['rank']

            # Create an embed to display the fight
            embed = discord.Embed(title="Challenging Dungeon! :crossed_swords:", color=0x00FF9900)
            embed.add_field(name=f"{username} HP :heart:", value=users[username]['health'], inline=True)
            embed.add_field(name=f"{enemy_name} HP :space_invader:", value=enemy_hp, inline=True)
            embed.set_image(url=enemy_img)

            # Send the embed
            fight_message = await message.channel.send(embed=embed)

            while True:
                # player's turn
                player_damage = random.randint(1, player_atk)
                enemy_hp -= player_damage
                # to make sure enemy hp doesn't go below 0
                enemy_hp = max(0, enemy_hp)

                # Update the embed
                embed.set_field_at(0, name=f"{enemy_name} HP :space_invader:", value=f"{enemy_hp}/100", inline=False)
                embed.description = f'You dealt {player_damage} damage to the enemy!'

                await fight_message.edit(embed=embed)

                if enemy_hp <= 0:
                    await message.channel.send('You win! You gained 10 gold!')
                    users[username]['wins'] += 1
                    users[username]['gold'] += 10

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
                users[username]['health'] -= enemy_damage
                # to make sure player hp doesn't go below 0
                users[username]['health'] = max(0, users[username]['health'])

                # Update the embed
                embed.set_field_at(1, name=f"{username} HP :heart:", value=f"{users[username]['health']}/{player_hp}",
                                   inline=False)
                embed.description = f'The enemy dealt {enemy_damage} damage to you!'
                await fight_message.edit(embed=embed)

                if users[username]['health'] <= 0:
                    users[username]['health'] += 60  # add 60hp back after player loses
                    if users[username]['gold'] > 0:
                        await message.channel.send('You lose! 1 Gold loss.')
                        users[username]['gold'] -= 1
                    else:
                        await message.channel.send('You lose!')
                    break

            # Update the previous rank for the user
            users[username]['previous_rank'] = previous_rank

    client.run(TOKEN)
