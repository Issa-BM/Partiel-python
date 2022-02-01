#!/usr/bin/env python
# coding: utf-8

# 2. Gestion des exceptions pour la fonction polynomiale

# In[12]:


def polynomiale(x) :
    
    ##########################
    ###Chaine de caractères###
    ##########################
    if(type(x) == str):
        print("Les chaînes de caractères ne sont pas prises en compte")
        print("Veuillez saisir un nombre : ")
        while (type(x) == str):
            try:
                x = int(input())
            except ValueError:
                print("Essayer avec un nombre")
    ##########################
    #########Complexe#########
    ##########################
    elif(type(x) == complex) : 
        print("Vous avez choisi un nombre complexe")
        print("Veuillez saisir un nombre positif : ")
        while (type(x) == complex):
            try:
                x = int(input())
            except ValueError:
                print("Essayer avec un nombre")
    ##########################
    #########Négatif##########
    ##########################
    elif(x < 0) :
        print("Vous avez choisi un nombre négatif")
        print("Très bon choix, vous allez découvrir le côté obscur des polynomes")
        return (x**3 -1.5*(x**2)-6*x+5)
    ##########################
    ######Grand nombre########
    ##########################
    elif(x > 10000) :
        print("Le nombre saisi est trop grand, il est supérieur à 10000")
        print("Veuillez saisir un nombre adapté : ")
        while (x > 10000):
            try:
                x = int(input())
            except ValueError:
                print("Essayer avec un nombre plus petit")
    ##########################
    ######Petit nombre########
    ##########################
    elif(x <10) :
        print("Le nombre saisi est assez petit, vous aurez pu le faire à la main")
        print("Voici quand même le résultat : ")
        return (x**3 -1.5*(x**2)-6*x+5)
    return (x**3 -1.5*(x**2)-6*x+5)

polynomiale(9)


# In[ ]:




