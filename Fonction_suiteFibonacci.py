#!/usr/bin/env python
# coding: utf-8

# 1.c) La fonction de la suite de Fibonnaci

# In[2]:


def suiteFibonacci() :
    x = int(input("Entrez un nombre : "))
    premierTerme = 0
    deuxiemeTerme = 1
    print("La suite fibonacci est : ")
    print(premierTerme,", ",deuxiemeTerme,end="") #Le end va nous permettre de ne pas aller à la ligne(Python 3)
    for i in range(2,x) :
        termeSuivant = premierTerme + deuxiemeTerme
        print(", ",termeSuivant,end="")
        premierTerme = deuxiemeTerme
        deuxiemeTerme = termeSuivant
        
suiteFibonacci()