def character_binary_search(list, target):
    for word in list:
        print([ord(character) for character in word])

if __name__ == '__main__':
    list = ['abc','abd', 'efg', 'xyz']
    isFound = character_binary_search(list, 'abd')
    print(isFound)