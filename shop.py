
#Lists shop items    
def shop_message(shop_items):
    count =0
    item_list = ''
    for x,y in shop_items.items():
        item_list += (str(count+1) +': '+x + '-> ' + str(y) +' gold\n') 
        count += 1
    return  item_list


                

