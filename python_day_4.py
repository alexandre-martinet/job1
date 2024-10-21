def add(a,b):
    result = a + b
    return result

print(add(4,4))

def my_print_hello():
    return("hello world")

print(my_print_hello())

def my_print_name(name):
    return name

print(my_print_name("alex"))

print(my_print_name("owen"))

print(add(55,42))

def GetHello():
    return ("Hello la Plateforme")
print(GetHello())





def calcul(num1,operator,num2):
    if operator == "+":
        return (num1+num2)
    elif operator == "*":
        return (num1*num2)
    elif operator == "-":
        return(num1-num2)
    elif operator == "/":
        return(num1/num2)
    elif operator == "%":
        return (num1%num2)
    else :
        return ("pas fonctionnel")

print(calcul(10,"/",2))

def nombre(a):
    if a > 0:
        return("positif")
    else :
        return ("négatif")


print(nombre(-2))

def langage(langage):
    if langage == "Javascript" :
        return ("tu es un developpeur web")
    elif langage == "python":
        return ("tu es un developpeur IA")
    elif langage == "java":
        return("tu es un developpeur logiciel")
    elif langage == "reactjs":
        return("tu es un developpeur mobile")
    else :
        return ("Un jour je serais le meilleur developpeur")
    
print(langage("python"))

def fruit_de_saison(type,saison):
    if type == "fruit" and saison == "hiver":
        return("orange,mandarine et kiwi")
    elif type == "fruit" and saison == "ete":
        return ("poire,fraise,cassis")
    elif type == "legume" and saison == "hiver":
        return ("carotte,topinambour,endive")
    elif type == "legume" and saison == "hiver":
        return ("artichaut,aubergine,navet")
    else :
        return("casse toi de là y a que des fruit !")

print(fruit_de_saison("fruit","ete"))

def moyenne(a,b,c):
    a = int(input("Saisir une note : "))
    b = int(input("Saisir une note : "))
    c = int(input("Saisir une note : "))
    moyenne_etudiant=(a+b+c)/3
    if 21 > moyenne_etudiant > 14:
        return ("Très bon élève")
    elif 15 > moyenne_etudiant > 10:
        return ("Bon élève")
    elif 11 > moyenne_etudiant > 7:
        return ("Eleve moyen")
    elif 8 > moyenne_etudiant > -1:
        return("Eleve devant faire des efforts")
    else :
        ("Veuillez entrer des chiffres entre 20 et 0")

print(moyenne(0,0,0))
