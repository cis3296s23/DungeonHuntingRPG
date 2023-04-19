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