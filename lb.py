import discord


users = {
    'Dark#6189': {
        'rank': 'F',
        'wins': 0,
        'gold': 0,  # gold gained from fighting monsters
        'inventory': {}  # inventory to store items from shop
    },
    'user2': {
        'rank': 'A',
        'wins': 3,
        'gold': 0,
        'inventory': {}
    },
    'user3': {
        'rank': 'A',
        'wins': 5,
        'gold': 0,
        'inventory': {}
    },
}

def leaderboard(dic):
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []


    for key in dic:
        if dic[key]['rank'] == 'A':
            a.append({key:dic[key]['wins']})
        elif dic[key]['rank'] == 'B':
            b.append({key:dic[key]['wins']})
        elif dic[key]['rank'] == 'C':
            c.append({key:dic[key]['wins']})
        elif dic[key]['rank'] == 'D':
            d.append({key:dic[key]['wins']})
        elif dic[key]['rank'] == 'E':
            e.append({key:dic[key]['wins']})
        elif dic[key]['rank'] == 'F':
            f.append({key:dic[key]['wins']})

    embed = discord.Embed(title="Leaderboard!", colour=discord.Color.from_rgb(255,255,0), description="Our Top 5 Players From Each Rank")
    embed.set_thumbnail(url="https://media.istockphoto.com/id/1176397624/vector/vector-flat-golden-trophy.jpg?s=612x612&w=0&k=20&c=kjnN3SB3l1cAMMt5xUvnyJDfPzQKzZ_pZHt3jaFnmF0=")
    embed.add_field(name="Rank A Users", value=list_to_string(a), inline=False)
    embed.add_field(name="Rank B Users", value=list_to_string(b), inline=False)
    embed.add_field(name="Rank C Users", value=list_to_string(c), inline=False)
    embed.add_field(name="Rank D Users", value=list_to_string(d), inline=False)
    embed.add_field(name="Rank E Users", value=list_to_string(e), inline=False)
    embed.add_field(name="Rank F Users", value=list_to_string(f), inline=False)

    return embed


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = []

    for item in sequence:
        if list(item.values())[0] > list(pivot.values())[0]:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort(items_greater) + [pivot] + quick_sort(items_lower)


def list_to_string(items):
    rank = ""
    new = quick_sort(items)
    for index, info in enumerate(new):
        if index == len(new) - 1:
            tmp = f"{list(info.keys())[0]}: {list(info.values())[0]} wins"
            rank += tmp
        else:
            tmp = f"{list(info.keys())[0]}: {list(info.values())[0]} wins\n"
            rank += tmp
    
    if len(rank) == 0:
        rank = "<none>"
    
    return rank
