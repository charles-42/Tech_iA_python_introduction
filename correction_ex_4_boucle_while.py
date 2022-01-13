"""**`Exercice 4`**: Plus classique et beaucoup moins drole 
- écrivez un programme script qui demande deux nombres puis renvoie leur somme si les nombres sont valides 
sinon il renvoie une erreur et demande à nouveaux deux nombres valides."""

# # première manière
# while True:
#     nb_1 = input("donnez moi un premier nombre")
#     nb_2 = input("donnez moi un autre nombre")

    
#     for c in nb_1:
#         if c not in ["0","1","2","3","4","5","6","7","8","9"]:
#             break
#         nb_1 = int(nb_1)

#     for c in nb_2:
#         if c not in ["0","1","2","3","4","5","6","7","8","9"]:
#             break
#         nb_2 = int(nb_2)

#     if isinstance(nb_1,int) and isinstance(nb_2,int):
#         break

#     print("Les valeurs renseignées ne sont pas des nombres")

# print( nb_1 + nb_2)

# # deuxième manière
while True:
    nb_1 = input("donnez moi un premier nombre")
    nb_2 = input("donnez moi un autre nombre")

    
    if set(list(nb_1)).issubset(["0","1","2","3","4","5","6","7","8","9"]):
        nb_1 = int(nb_1)

    if set(list(nb_2)).issubset(["0","1","2","3","4","5","6","7","8","9"]):
        nb_2 = int(nb_2)

    if isinstance(nb_1,int) and isinstance(nb_2,int):
        break

    print("Les valeurs renseignées ne sont pas des nombres")

print( nb_1 + nb_2)


# # deuxième manière



while True:
    nb_1 = input("donnez moi un premier nombre")
    nb_2 = input("donnez moi un autre nombre")

    try :
        nb_1 = int(nb_1)
        nb_2 = int(nb_2)
        print( nb_1 / nb_2)
        break
    except ValueError :
        print("Les valeurs renseignées ne sont pas des nombres")
    except ZeroDivisionError :
        print("On ne peut pas diviser par zéro, chisissez un autre nombre 2")



