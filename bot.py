# Discord bot commands
import random
import discord
import responses
import shop

CHANNEL_ID = 1075850854126583900
BOT_TOKEN = 'MTA3NTg0NjQ5MTE4MjIyMzQ5MA.G3s9Ur.flL-cn6jxVJOtdNoncU4YEtOC8Rb9yZxMG-BUw'  # remove before committing


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
        'wins': 0,
        'gold': 0, # gold gained from fighting monsters
        'inventory':{} #inventory to store items from shop
    },
    'user2': {
        'rank': 'F',
        'wins': 0,
        'gold' : 0,
        'inventory':{}
    },
}

shop_items = {   # shop, displays items and the amount of gold for them
    'dull sword': 10,
    'shape sword': 40,
    'great sword': 100,
    'light armor': 20,
    'medium armor': 50,
    'heavy armor': 100,
    'health potion': 10 
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

        if username not in users:
            users[username] = {
                'rank': 'F',
                'wins': 0,
                'gold':0,
                'inventory': {}
            }


        if user_message[0] == '?':  # If the message starts with a question mark
            user_message = user_message[1:]  # "?Help" -> "Help", i.e., ignores the question mark
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


        # Check stats
        if user_message == '!stat':
            embed = discord.Embed(colour=discord.Color.from_rgb(247, 38, 42), title=username + '\'s stats\n',
                                  description=f'Rank: {users[username]["rank"]}\n' +
                                              f'Wins: {users[username]["wins"]}\n' + 
                                              f'Gold: {users[username]["gold"]}\n')
            await message.channel.send(embed=embed)

        if user_message == '!shop': #opens shop menu
            await message.channel.send( "Welcome to the shop!\nSwords increase your damage output, armors help reduce enemy damage, and health potions restore your health.\n")
            await message.channel.send( "Please enter the number of the item you wish to purchase.\n")
            await message.channel.send(  shop.shop_message(shop_items)) #lists shop items
            
            
        #Buy and store item into player's inventory        
        if  user_message == '1' or user_message == '2' or user_message == '3' or user_message == '4' or user_message == '5' or user_message == '6' or user_message == '7':         

            temp = user_message
            num = int(temp) - 1
            item = list(shop_items)

    
            if( users[username]["gold"] >= shop_items[item[num]]   ): #checks if player have enough gold
                if item[num] not in users[username]['inventory']:
                    users[username]['inventory'][item[num]] = 1   #add shop item into player inventory 
                else:
                    users[username]['inventory'][item[num]] += 1

                users[username]["gold"] -= shop_items[item[num]]        #take gold from player

                await message.channel.send( item[num] + ' obtained!\n')        
            else:
                await message.channel.send('Not enought gold!\n')


        
    
        if user_message == '!inventory': #open user's inventory
            if(bool(users[username]["inventory"]) != False): #check if inventory is full 
                in_count = 0
                for x,y in users[username]["inventory"].items():
                    await message.channel.send(str(in_count +1) + ' = '+ x + ' : '+ str(y))
                    in_count+= 1    
            else:
                await message.channel.send('Empty inventory. You can visit the shop to purchase items by using the \'!shop\' command.\n')
           
        
        

        # RPG stuff
        if message.content.startswith('!fight'):
            username = str(message.author)

            # If the user is new, initialize their rank to F and wins to 0
            if username not in users:
                users[username] = {
                    'rank': 'F',
                    'wins': 0,
                    'gold':0,
                    'inventory': {}
                }

            player_hp = 100
            enemy_hp = 10
            player_attack = 10
            enemy_attack = 10

            # Store the previous rank before the fight
            previous_rank = users[username]['rank']

            # Create an embed to display the fight
            embed = discord.Embed(title="Challenging Dungeon! :crossed_swords:", color=0x00FF9900)
            embed.add_field(name="Player HP :heart:", value=player_hp, inline=True)
            embed.add_field(name="Enemy HP :space_invader:", value=enemy_hp, inline=True)

            # add image
            embed.set_image(
                url="https://static.wikia.nocookie.net/solo-leveling/images/e/e8/Centipede1.jpg/revision/latest/scale-to-width-down/350?cb=20210628033630")

            # Send the embed
            fight_message = await message.channel.send(embed=embed)

            while True:
                # player's turn
                player_damage = random.randint(1, player_attack)
                enemy_hp -= player_damage

                # Update the embed
                embed.set_field_at(0, name="Enemy HP :space_invader:", value=f"{enemy_hp}/100", inline=False)
                embed.description = f'You dealt {player_damage} damage to the enemy!'

                await fight_message.edit(embed=embed)

                if enemy_hp <= 0:
                    await message.channel.send('You win! You gained 10 gold!')
                    users[username]['wins'] += 1
                    users[username]['gold'] += 10

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

                # Update the embed
                embed.set_field_at(1, name="Player HP :hearts:", value=f"{player_hp}/100", inline=False)
                embed.description = f'The enemy dealt {enemy_damage} damage to you!'
                await fight_message.edit(embed=embed)

                if player_hp <= 0:
                           
                    if(users[username]['gold'] > 0):
                        await message.channel.send('You lose! 1 Gold loss.')
                        users[username]['gold'] -= 1
                    else:
                        await message.channel.send('You lose!')
                    break

            # Update the previous rank for the user
            users[username]['previous_rank'] = previous_rank

    client.run(TOKEN)
