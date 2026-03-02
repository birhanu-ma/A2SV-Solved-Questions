def dominantCharacter(t,num_string,character):
    if "aa" in character:
        return 2
    elif "aba" in character or "aca" in character:
        return 3
    elif "abca"  in character or "acba" in character:
        return 4
    elif "abbacca" in character  or "accabba" in character:
            return 7
    else:
         return -1


t =  int(input())

for _ in range(t):
    num_string = str(input())
    character = str(input())  
    print(dominantCharacter(t,num_string,character )) 
     
