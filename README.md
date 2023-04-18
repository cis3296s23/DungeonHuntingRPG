# Dungeon Hunting RPG
Dungeon Hunting RPG is an application that runs as a discord bot that allows users to play a dungeon hunting minigame via discord. The bot sets up 
enemies for the players to fight, dungeons to explore, checking of current adventure guild rank, displaying their health bars, and more. The players
interact with the bot with commands to decide what actions they want to take. 
### Requirements
 - A bit of experience with python & terminal (i.e. know how to use pip install)
# How to run
 - Download the latest [release](https://github.com/cis3296s23/DungeonHuntingRPG/releases)
 - Open the code in an IDE/terminal and move files into the directory of the project
 - Setup Discord bot as shown in [Technical Information](#technical-information)
 - Right click the channel you want your Discord bot to be in and copy the Channel ID
 - In bot.py, enter the Discord Bot Token & Channel ID into the section shown below
```
CHANNEL_ID = 
BOT_TOKEN = 'enter token here'
```
- Install Discord API
  - Go to terminal, and enter below
```
pip install discord.py 
```
-  Run main.py, and the discord bot should run in the server
-  **CAUTION TO DEVELOPERS**: remember to erase the token from TOKEN = 'erase token here' before releasing any changes to public, not doing so will require you to create a new discord bot token

# Technical Information 

## Enable Developer Mode

1. Open the discord application.
2. On the bottom left corner of the application, click the cog wheel settings icon.
3. Go to the "Advanced" section and tick on "Developer Mode".
![Screenshot (992)](https://user-images.githubusercontent.com/74037708/231637902-45067602-20ef-49fd-b115-6e21ccc6e2ff.png)

## Setup Discord Bot

1. Navigate to the [Discord Developer Portal](https://discord.com/developers/applications) and click New Application

![CreateApp](https://user-images.githubusercontent.com/74037708/231640358-57cb2073-f6d6-4036-953b-ff9ac4f3330b.png)

2. Create a name then navigate to the Bot tab then click Add Bot
![AddBot](https://user-images.githubusercontent.com/74037708/231640364-a6253cc7-aba3-4cbf-8da3-d6c81ada4441.png)
3. Press View Token and then Copy your bot's token
![CopyToken](https://user-images.githubusercontent.com/74037708/231640369-ad5225f2-c17f-423c-8b15-bc8d821c3b1e.png)
4. Scroll down until you see "MESSAGE CONTENT INTENT" and enable it
![Intent](https://user-images.githubusercontent.com/74037708/231642535-a5fed24a-8eeb-43b0-96a9-5bd6446fda05.png)

## Add Discord Bot to Server

1. Make sure you're logged on to the [Discord website](https://discord.com/).
2. Navigate to the [Discord Developer Portal](https://discord.com/developers/applications).
3. Click on your bot's page.
4. Go to the "OAuth2" tab and click "URL Generator". 
5. Tick the "bot" checkbox under "scopes".
6. Tick the permissions required for your bot to function under "Bot Permissions" (Please be aware of the consequences of requiring your bot to have "Administrator" permission, look at the image below for a base configuration).
![Instruct](https://user-images.githubusercontent.com/74037708/231643793-6008b628-bc23-43e9-803c-f9d8a7cb1726.png)
7. Now the resulting URL can be used to add your bot to a server. Copy and paste the URL into your browser, and choose a server to invite the bot to (will only allow the bot to be invited to servers where you have the "Manage Server" permissions). Then click "Authorize".
