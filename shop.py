# Lists shop items
def shop_message(shop_items):
    """
    Returns a string of the shop items
    :param shop_items: a dictionary of shop items
    :return: a string of the shop items
    """
    count = 0
    item_list = ''
    for x, y in shop_items.items():
        item_list += (str(count + 1) + ': ' + x + '-> ' + str(y) + ' gold\n')
        count += 1
    return item_list
