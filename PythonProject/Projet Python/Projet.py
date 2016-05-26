#Pierre, feuille, ciseaux, lézard, spock

from random import *
from tkinter import *
import time

def game():
    Play()

def Play():
    p1 = 0
    p2 = 0
    while p1 <= 2 or p2 <= 2:
        choice()
        IA = randint(1,5)
        print(str(IA)+'\n')
        if Move==1:
            if IA == 2 or IA == 5:
                p2 = p2 + 1
                print('IA gagne')
            elif IA == 3 or IA == 4:
                p1 = p1 + 1
                print('Joueur gagne')
            elif IA == 1:
                print('Egalité')
        if Move==2:
            if IA == 3 or IA == 4:
                p2 = p2 + 1
                print('IA gagne')
            elif IA == 1 or IA == 5:
                p1 = p1 + 1
                print('Joueur gagne')
            elif IA == 2:
                print('Egalité')
        if Move==3:
            if IA == 1 or IA == 5:
                p2 = p2 + 1
                print('IA gagne')
            elif IA == 2 or IA == 4:
                p1 = p1 + 1
                print('Joueur gagne')
            elif IA == 3:
                print('Egalité')
        if Move==4:
            if IA == 1 or IA == 3:
                p2 = p2 + 1
                print('IA gagne')
            elif IA == 2 or IA == 5:
                p1 = p1 + 1
                print('Joueur gagne')
            elif IA == 4:
                print('Egalité')
        if Move==5:
            if IA == 2 or IA == 4:
                p2 = p2 + 1
                print('IA gagne')
            elif IA == 1 or IA == 3:
                p1 = p1 + 1
                print('Joueur gagne')
            elif IA == 5:
                print('Egalité')
        if p1==2:
            return('You win!')
        elif p2==2:
            return('You loose')
    

def Rock():
    if Button['text']=='Pierre':
        Move=1
    elif Button['text']=='Feuille':
        Move=2
    elif Button['text']=='Ciseaux':
        Move=3
    elif Button['text']=='Lézard':
        Move=4
    elif Button['text']=='Spock':
        Move=5

def change():
    global can
    global photo
    global photo2
    global s
    global i
    while i <=3:
        if s==0:
            s=1
            i=i+1
            photo = PhotoImage(file="B2.png")
            photo2 = PhotoImage(file="T1.png")
            can.create_image(0,300, anchor = NW, image=photo)
            can.create_image(0,175, anchor = NW, image=photo2)
        elif s==1:
            s=0
            i=i+1
            photo = PhotoImage(file="B1.png")
            can.create_image(0,300, anchor = NW, image=photo)
        can.pack(side=TOP, padx=5, pady=5)

def change2():
    can.after(300, change)



#Heads
def loseround():
    global photo2
    photo2 = PhotoImage(file="T1.png")
    can.create_image(0,175, anchor = NW, image=photo2)
    can.pack(side=TOP, padx=5, pady=5)

def losegame():
    global photo2
    photo2 = PhotoImage(file="T3.png")
    can.create_image(0,175, anchor = NW, image=photo2)
    can.pack(side=TOP, padx=5, pady=5)

def winround():
    global photo2
    photo2 = PhotoImage(file="Win.png")
    can.create_image(0,175, anchor = NW, image=photo2)
    can.pack(side=TOP, padx=5, pady=5)

def wingame():
    global photo2
    photo2 = PhotoImage(file="Win.png")
    can.create_image(0,175, anchor = NW, image=photo2)
    can.pack(side=TOP, padx=5, pady=5)

#Move

def shake():
    global photo
    photo = PhotoImage(file="B2.png")
    can.create_image(0,300, anchor = NW, image=photo)
    can.pack(side=TOP, padx=5, pady=5)

def reverseshake():
    global photo
    photo = PhotoImage(file="B1.png")
    can.create_image(0,300, anchor = NW, image=photo)
    can.pack(side=TOP, padx=5, pady=5)

#Image pour le joueur
def rock():
    global photo3
    photo3 = PhotoImage(file="Rock.png")
    can.create_image(0,0, anchor = NW, image=photo3)
    can.pack(side=TOP, padx=5, pady=5)

def paper():
    global photo3
    photo3 = PhotoImage(file="Paper.png")
    can.create_image(0,0, anchor = NW, image=photo3)
    can.pack(side=TOP, padx=5, pady=5)

def scissors():
    global photo3
    photo3 = PhotoImage(file="Scissors.png")
    can.create_image(0,0, anchor = NW, image=photo3)
    can.pack(side=TOP, padx=5, pady=5)

def lizard():
    global photo3
    photo3 = PhotoImage(file="Lizard.png")
    can.create_image(0,0, anchor = NW, image=photo3)
    can.pack(side=TOP, padx=5, pady=5)

def spock():
    global photo3
    photo3 = PhotoImage(file="Spock.png")
    can.create_image(0,0, anchor = NW, image=photo3)
    can.pack(side=TOP, padx=5, pady=5)

#Image pour l'IA
    
def rock():
    global photo4
    photo4 = PhotoImage(file="Rock.png")
    can.create_image(350,250, anchor = NW, image=photo4)
    can.pack(side=TOP, padx=5, pady=5)

def paper():
    global photo4
    photo4 = PhotoImage(file="Paper.png")
    can.create_image(350,250, anchor = NW, image=photo4)
    can.pack(side=TOP, padx=5, pady=5)

def scissors():
    global photo4
    photo4 = PhotoImage(file="Scissors.png")
    can.create_image(350,250, anchor = NW, image=photo4)
    can.pack(side=TOP, padx=5, pady=5)

def lizard():
    global photo4
    photo4 = PhotoImage(file="Lizard.png")
    can.create_image(350,250, anchor = NW, image=photo4)
    can.pack(side=TOP, padx=5, pady=5)

def spock():
    global photo4
    photo4 = PhotoImage(file="Spock.png")
    can.create_image(350,250, anchor = NW, image=photo4)
    can.pack(side=TOP, padx=5, pady=5)


def supprime():
    can.delete("all")

def rules():
    can.delete("all")
    global sheldon
    global rules
    sheldon = PhotoImage(file="Sheldon.png")
    can.create_image(0,200, anchor = NW, image=sheldon)
    rules = PhotoImage(file="Rules.png")
    can.create_image(150,0, anchor = NW, image=rules)

def go():
    can.delete("all")
    global photo
    global photo2
    global AI
    photo = PhotoImage(file="B1.png")
    photo2 = PhotoImage(file="Base.png")
    AI = PhotoImage(file="IA.png")
    can.create_image(0,300, anchor = NW, image=photo2)
    can.create_image(300,0, anchor = NW, image=AI)
    can.create_image(0,300, anchor = NW, image=photo)
    can.pack(side=TOP, padx=5, pady=5)



fenetre= Tk()
            
can= Canvas(fenetre, width=500, height=400, bg='white')
photo = PhotoImage(file="B1.png")
photo2 = PhotoImage(file="Base.png")
AI = PhotoImage(file="IA.png")
can.create_image(0,300, anchor = NW, image=photo2)
can.create_image(300,0, anchor = NW, image=AI)
can.create_image(0,300, anchor = NW, image=photo)
can.pack(side=TOP, padx=5, pady=5)

b1=Button(fenetre, text ='Pierre', command=supprime)
b2=Button(fenetre, text ='Feuille', command=change2)
b3=Button(fenetre, text ='Ciseaux', command=rules)
b4=Button(fenetre, text ='Lézard', command=go)
b5=Button(fenetre, text ='Spock', command=choice)
b1.pack(side=LEFT, padx=8, pady=8)
b2.pack(side=LEFT, padx=8, pady=8)
b3.pack(side=LEFT, padx=8, pady=8)
b4.pack(side=LEFT, padx=8, pady=8)
b5.pack(side=LEFT, padx=8, pady=8)

i=0
s=0
fenetre.mainloop()






    
