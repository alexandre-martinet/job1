chaine = "abcdefghijklmnopqrstuvwxyz" * 5

for i in range(1, len(chaine),2):
    if len(chaine[:i]) >= i:
        print(chaine[:i])
    else:
        break
