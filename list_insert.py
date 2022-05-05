def insert_henny(list, index, value):
    if index > len(list)-1:
        list.append(value)
    elif index < 0:
        raise Exception("Index must be postive")
    else:
        # insert
        print('need to insert')
        new_val = value
        for i in range(index, len(list)):
            old_val = list[i]
            list[i] = new_val
            new_val = old_val
        list.append(new_val)
    return list


# raises exception
new_list1 = insert_henny([4, 5, 6, 3], -1, 10)
# appends the value
new_list2 = insert_henny([4, 5, 6, 3], 10, 10)
# inserts the value
new_list3 = insert_henny([4, 5, 6, 3], 1, 10)
