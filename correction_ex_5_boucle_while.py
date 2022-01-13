"""
**`Mini-projet`**: liste de courses
Creez un programme script qui propose ce menu (et permet bien de le réaliser)

Choisissez par les options suivantes:
- 1: ajoutez un élément à la liste
- 2: retirer une élément de la liste
- 3: afficher la liste
- 4: vider la liste
- 5: Quitter  
**Quel est votre choix?:**

"""

menu = """
- 1: ajoutez un élément à la liste
- 2: retirer une élément de la liste
- 3: afficher la liste
- 4: vider la liste
- 5: Quitter 
"""

reponse = int()
ma_liste_de_course = []
while reponse != "5":  
    print(menu)
    reponse = input("Que voulez vous faire?")
    
    if reponse not in ["1","2","3","4","5"]:
        print("ceci n'est pas une réponse possible")

    elif reponse == "1":
        element = input("que voulez vous ajouter à votre liste de course?")
        ma_liste_de_course.append(element)
    
    elif reponse == "2":
        element_a_retirer = input("que voulez vous retirez à votre liste de course?")
        if element_a_retirer in ma_liste_de_course:
            ma_liste_de_course.remove(element_a_retirer)
        else:
            print("ce n'est pas dans votre liste de course")

    elif reponse == "3":
        print(ma_liste_de_course)

    elif reponse == "4":
        ma_liste_de_course.clear()

    