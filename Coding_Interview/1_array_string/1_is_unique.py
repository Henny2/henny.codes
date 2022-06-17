# A) Implement an algorithm to determine if a string has all unique characters.

def is_unique(s):
    character_counts = {}
    for character in s:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    # print(character_counts)
    for char in character_counts:
        if character_counts[char] > 1:
            print('not unique')
            return False
    print('unique')
    return True


print(is_unique('helo'))


# B) What if you cannot use additional data structures?
def is_unique_plain(s):
    string_length = len(s)

    for i in range(0, string_length-1):
        print(f'i: {i}')
        for j in range(i+1, string_length):
            print(f'j: {j}')
            if s[i] == s[j]:
                return False

    return True


print(is_unique_plain('hello'))


# this ends up being a tradeoff between time and space complexity
