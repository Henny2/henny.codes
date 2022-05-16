# list_test = ['hello', 'bye', 'henny']
# print(','.join(l for l in list_test))

test_dict = {
    'col1': 'alias1',
    'col2': 'alias2'
}
input_table = 'f_HENNY'
select = 'SELECT '
counter = 0
for col in test_dict:
    print(col)
    print(test_dict[col])
    select_line = f'{col} as {test_dict[col]}'
    print(select_line)

    select += select_line
    counter += 1
    if counter == len(test_dict):
        continue
    select += ','
select += f' FROM <INPUT:{input_table}>'
print(select)

# print(f'Select {list_dict}')

# print(isinstance([4, 5, 4], list))
