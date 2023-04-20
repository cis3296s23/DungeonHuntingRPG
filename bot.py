# Discord bot commands
import random
import discord
import shop
import lb
import data

CHANNEL_ID = 1075850854126583900
BOT_TOKEN = 'enter your token'  # remove before committing


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

        if username not in data.users:
            data.users[username] = {
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
                                  description=f'Rank: {data.users[username]["rank"]}\n' +
                                              f'Wins: {data.users[username]["wins"]}\n' +
                                              f'Gold: {data.users[username]["gold"]}\n' +
                                              f'Health: {data.users[username]["health"]}\n'
                                              f'Weapon: {data.users[username]["weapon_equip"]}\n' +
                                              f'Armor: {data.users[username]["armor_equip"]}\n')
            embed.set_thumbnail(
                url="https://preview.redd.it/zhrpsafn97891.png?width=608&format=png&auto=webp&s=31b67183885b9b4bce3d74f01c95e85f61201cd0")
            await message.channel.send(embed=embed)

        if user_message == '!shop':  # opens shop menu
            embed = discord.Embed(title="Welcome to the shop!",
                                  description="Swords increase your damage output, armors help reduce enemy damage, and health potions restore your health.",
                                  color=0x3D85C6)
            embed.add_field(name="Shop Items", value=shop.shop_message(data.shop_items), inline=False)
            embed.set_thumbnail(
                url="https://static.wikia.nocookie.net/solo-leveling/images/9/95/System1.jpg/revision/latest?cb=20210625162338")
            embed.set_footer(text="Enter the number of the item you want to buy.")
            await message.channel.send(embed=embed)

        # Buy and store item into player's inventory
        if user_message == '1' or user_message == '2' or user_message == '3' or user_message == '4' or user_message == '5' or user_message == '6' or user_message == '7':

            temp = user_message
            num = int(temp) - 1
            item = list(data.shop_items)

            if data.users[username]["gold"] >= data.shop_items[item[num]]:  # checks if player have enough gold
                if item[num] not in data.users[username]['inventory']:
                    data.users[username]['inventory'][item[num]] = 1  # add shop item into player inventory
                else:
                    data.users[username]['inventory'][item[num]] += 1

                data.users[username]["gold"] -= data.shop_items[item[num]]  # take gold from player

                await message.channel.send(item[num] + ' obtained!\n')
            else:
                await message.channel.send('Not enought gold!\n')

        if user_message == '!inventory':  # open user's inventory
            inventory = data.users[username]["inventory"]
            weapon_equip = data.users[username]['weapon_equip']
            armor_equip = data.users[username]['armor_equip']

            if bool(inventory) != False:  # check if inventory is full
                embed = discord.Embed(title="Inventory")
                embed.add_field(name="Weapon equipped", value=weapon_equip)
                embed.add_field(name="Armor equipped", value=armor_equip)
                # embed.add_field(name="\u200b", value="\u200b", inline=False)
                embed.add_field(name="Items", value="\n", inline=False)
                embed.set_thumbnail(
                    url="https://static.wikia.nocookie.net/solo-leveling/images/0/01/SystemInventory1.jpg/revision/latest?cb=20210625162158")

                for item, count in inventory.items():
                    if item == 'health potion':

                        embed.add_field(name=item, value=f"- {count}")
                    else:
                        embed.add_field(name=item, value=f"")

                embed.set_footer(text="Enter the name of the item you want to equip or use.")
                await message.channel.send(embed=embed)

            else:
                await message.channel.send(
                    'Empty inventory. You can visit the shop to purchase items by using the \'!shop\' command.\n')

        for player_item in data.shop_items:
            if user_message == player_item:
                if player_item in data.users[username]['inventory']:  # check if in inventory
                    if ("health potion" in player_item) == True:  # if it is a sword
                        if data.users[username]['inventory']['health potion'] >= 1:
                            await message.channel.send('Potion used, +10 health.\n')
                            data.users[username]['inventory'][player_item] -= 1
                            data.users[username]['health'] += 10
                        else:
                            await message.channel.send(
                                'No potions left in inventory, please visit the shop for more.\n')
                    else:
                        if ("sword" in player_item) == True:  # if it is a sword
                            data.users[username]['weapon_equip'] = player_item
                        elif ("armor" in player_item) == True:  # if it is an armor
                            data.users[username]['armor_equip'] = player_item
                        await message.channel.send(player_item + ' equipped!\n')

        # Leaderboard feature
        if user_message == '!lb':
            embed = lb.leaderboard(data.users)
            await message.channel.send(embed=embed)

        # RPG stuff
        if message.content.startswith('!fight'):
            username = str(message.author)

            # If the user is new, initialize their rank to F and wins to 0
            if username not in data.users:
                data.users[username] = {
                    'rank': 'F',
                    'wins': 0,
                    'gold': 0,
                    'inventory': {},
                    'weapon_equip': 'No weapons equipped',
                    'armor_equip': 'No armor equipped',
                    'health': 100
                }

            rank = data.users[username]['rank']

            # Check if the user has reached the required number of wins for their rank
            if data.users[username]['wins'] >= data.ranks[rank]['wins_required']:
                enemy_name = data.ranks[rank]['enemy']
            else:
                # If the user hasn't reached the required number of wins, they fight their previous enemy
                enemy_name = data.enemies[data.users[username]['previous_enemy']]['name']

            enemy = data.enemies[enemy_name]
            enemy_hp = enemy['hp']
            enemy_atk = enemy['atk']
            enemy_img = enemy['img']
            data.users[username]['previous_enemy'] = enemy_name

            # player_hp = 100

            player_atk = 10

            for add_dmg in data.weapon_dmg:  # add additional player dmg if weapon is equipped
                if data.users[username]['weapon_equip'] == add_dmg:
                    player_atk += data.weapon_dmg[add_dmg]

            for add_health in data.armor_health:  # add additional player dmg if weapon is equipped
                if data.users[username]['armor_equip'] == add_health:
                    # player_hp += armor_health[add_health]
                    data.users[username]['health'] += data.armor_health[add_health]

            player_hp = data.users[username]['health']

            # Store the previous rank before the fight
            previous_rank = data.users[username]['rank']

            # Create an embed to display the fight
            embed = discord.Embed(title="Challenging Dungeon! :crossed_swords:", color=0x00FF9900)
            embed.add_field(name=f"{username} HP :heart:", value=data.users[username]['health'], inline=True)
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
                    data.users[username]['wins'] += 1
                    data.users[username]['gold'] += 10

                    # Check if the user qualifies for a promotion
                    for rank in sorted(data.ranks, key=lambda x: data.ranks[x]['wins_required'], reverse=True):
                        if data.users[username]['wins'] >= data.ranks[rank]['wins_required']:
                            if rank != data.users[username]['rank']:
                                data.users[username]['rank'] = rank
                                await message.channel.send(
                                    f'Congratulations, {username}! You have been promoted to rank {rank}!')
                            break
                    break
                # enemy's turn
                enemy_damage = random.randint(1, enemy_atk)
                data.users[username]['health'] -= enemy_damage
                # to make sure player hp doesn't go below 0
                data.users[username]['health'] = max(0, data.users[username]['health'])

                # Update the embed
                embed.set_field_at(1, name=f"{username} HP :heart:",
                                   value=f"{data.users[username]['health']}/{player_hp}",
                                   inline=False)
                embed.description = f'The enemy dealt {enemy_damage} damage to you!'
                await fight_message.edit(embed=embed)

                if data.users[username]['health'] <= 0:
                    data.users[username]['health'] += 60  # add 60hp back after player loses
                    if data.users[username]['gold'] > 0:
                        await message.channel.send('You lose! 1 Gold loss.')
                        data.users[username]['gold'] -= 1
                    else:
                        await message.channel.send('You lose!')
                    break

            # Update the previous rank for the user
            data.users[username]['previous_rank'] = previous_rank

    client.run(TOKEN)
