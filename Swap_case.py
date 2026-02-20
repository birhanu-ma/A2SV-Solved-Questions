
def swap_case(s):
    character = []
    for char in s:
        if char == char.lower():
            character.append(char.upper())
        else:
            character.append(char.lower())
    return "".join(character)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)