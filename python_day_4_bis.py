def verif(a):
    if isinstance(a,int) and a > 0:
        if a % 2 == 0:
            return("le nombre  est pair.")
        else:
            return("Le nombre est impair.")
    else:
        return("le nombre est pas positif ou n'est pas entier")

print(verif(7))
print(verif(3))
print(verif(0.5))

def time_to_text(a):
    heure = a// 60
    
    minute = (a-(60*heure))
    
    temps = (heure,minute)
    return temps

resultat = (time_to_text(150))

print("%d heures et %d minutes"%(resultat[0],resultat[1]))

def string(mot):
    mot_inverse=mot[::-1]
    return(mot_inverse)
            

print(string("anakin"))
