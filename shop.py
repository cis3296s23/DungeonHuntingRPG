
#Lists shop items    
def shop_message(shop_items):
    count =0
    item_list = ''
    for x,y in shop_items.items():
        item_list += (str(count+1) +': '+x + '-> ' + str(y) +' gold\n') 
        count += 1
    return  item_list

def item_num(user_message):
    if user_message == '1':
        return 1
    if user_message == '2':
        return 2 
    if user_message == '3':
        return 3 
    if user_message == '4':
        return 4 
    if user_message == '5':
        return 5 
    if user_message == '6':
        return 6 
    if user_message == '7':
        return 7 
                

