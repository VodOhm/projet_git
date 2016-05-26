#Rock, Paper, Cisors, Lizard, Spock

from random import *
from tkinter import *
from tkinter.messagebox import *
import time

p1 = 0
p2 = 0
name =""

def Play(Move):
    global p1
    global p2
    IA = randint(1,5)
    print("Value AI:"+str(IA)+'\n')
    if Move==1:
        P_rock()
        if IA == 2 or IA == 5:
            p2 = p2 + 1
            print('AI wins')
            loseround()
            if IA == 2:
                AI_paper()
                label_results.config(text='AI did Paper, AI wins')
            if IA == 5:
                AI_spock()
                label_results.config(text='AI did Spock, AI wins')
            label_results.pack()
        elif IA == 3 or IA == 4:
            p1 = p1 + 1
            print('Player wins')
            winround()
            if IA == 3:
                AI_scissors()
                label_results.config(text='AI did Cisors, Player wins')
            if IA == 4:
                AI_lizard()
                label_results.config(text='AI did Lizard, Player wins')
            label_results.pack()
        elif IA == 1:
            AI_rock()
            print('Even')
            label_results.config(text='Even')
            label_results.pack()
    if Move==2:
        P_paper()
        if IA == 3 or IA == 4:
            p2 = p2 + 1
            print('AI wins')
            loseround()
            if IA == 3:
                AI_scissors()
                label_results.config(text='AI did Cisors, AI wins')
            if IA == 4:
                AI_lizard()
                label_results.config(text='AI did Lizard, AI wins')
            label_results.pack()
        elif IA == 1 or IA == 5:
            p1 = p1 + 1
            print('Player wins')
            winround()
            if IA == 1:
                AI_rock()
                label_results.config(text='AI did Rock, Player wins')
            if IA == 5:
                AI_spock()
                label_results.config(text='AI did Spock, Player wins')
            label_results.pack()
        elif IA == 2:
            AI_paper()
            print('Even')
            label_results.config(text='Even')
            label_results.pack()
    if Move==3:
        P_scissors()
        if IA == 1 or IA == 5:
            p2 = p2 + 1
            print('AI wins')
            loseround()
            if IA == 1:
                AI_rock()
                label_results.config(text='AI did Rock, AI wins')
            if IA == 5:
                AI_spock()
                label_results.config(text='AI did Spock, AI wins')
            label_results.pack()
        elif IA == 2 or IA == 4:
            p1 = p1 + 1
            print('Player wins')
            winround()
            if IA == 2:
                AI_paper()
                label_results.config(text='AI did Paper, Player wins')
            if IA == 4:
                AI_lizard()
                label_results.config(text='AI did Lizard, Player wins')
            label_results.pack()
        elif IA == 3:
            print('Even')
            AI_scissors()
            label_results.config(text='Even')
            label_results.pack()
    if Move==4:
        P_lizard()
        if IA == 1 or IA == 3:
            p2 = p2 + 1
            print('AI wins')
            loseround()
            if IA == 1:
                AI_rock()
                label_results.config(text='AI did Rock, AI wins')
            if IA == 3:
                AI_scissors()
                label_results.config(text='AI did Cisors, AI wins')
            label_results.pack()
        elif IA == 2 or IA == 5:
            p1 = p1 + 1
            print('Player wins')
            winround()
            if IA == 2:
                AI_paper()
                label_results.config(text='AI did Paper, Player wins')
            if IA == 5:
                AI_spock()
                label_results.config(text='AI did Spoke, Player wins')
            label_results.pack()
        elif IA == 4:
            print('Even')
            AI_lizard()
            label_results.config(text='Even')
            label_results.pack()
    if Move==5:
        P_spock()
        if IA == 2 or IA == 4:
            p2 = p2 + 1
            print('AI wins')
            loseround()
            if IA == 2:
                AI_paper()
                label_results.config(text='AI did Paper, AI wins')
            if IA == 4:
                AI_lizard()
                label_results.config(text='AI did Lizard, AI wins')
            label_results.pack()
        elif IA == 1 or IA == 3:
            p1 = p1 + 1
            print('Player wins')
            winround()
            if IA == 1:
                AI_rock()
                label_results.config(text='AI did Rock, Player wins')
            if IA == 3:
                AI_scissors()
                label_results.config(text='AI did Cisors, Player wins')
            label_results.pack()
        elif IA == 5:
            AI_spock()
            print('Even')
            label_results.config(text='Even')
            label_results.pack()
    if p1 == 2:
        print('\nYou wins !\n')
        wingame()
        victory()
    elif p2 == 2:
        print('\nThe computer beats you, SKYNET is on his way!\n')
        losegame()
        defeat()
    else:
        print('\nNext round !\n')

#def choice():  
#    if Button.text=='Rock':
#        Move=1
#    elif Button['text']=='Paper':
#        Move=2
#    elif Button['text']=='Cisors':
#        Move=3
#    elif Button['text']=='Lizard':
#        Move=4
#    elif Button['text']=='Spock':
#        Move=5

def touche_pressed():
    def touche_x(event):
        touche = event.keysym
        print(touche)
#        b1.config(relief=FLAT)
#        time.sleep(1)
        shake()
        Play(1)

    def touche_c(event):
        touche = event.keysym
        print(touche)
        shake()
        Play(2)

    def touche_v(event):
        touche = event.keysym
        print(touche)
        shake()
        Play(3)

    def touche_b(event):
        touche = event.keysym
        print(touche)
        shake()
        Play(4)

    def touche_n(event):
        touche = event.keysym
        print(touche)
        shake()
        Play(5)

    #Choppage de l'appui sur la touche x
    can.focus_set()
    can.bind("<KeyPress-x>", touche_x)
    #Choppage de l'appui sur la touche c
    can.focus_set()
    can.bind("<KeyPress-c>", touche_c)
    #Choppage de l'appui sur la touche v
    can.focus_set()
    can.bind("<KeyPress-v>", touche_v)
    #Choppage de l'appui sur la touche b
    can.focus_set()
    can.bind("<KeyPress-b>", touche_b)
    #Choppage de l'appui sur la touche n
    can.focus_set()
    can.bind("<KeyPress-n>", touche_n)

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
    photo2 = PhotoImage(file="Win2.png")
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
def P_rock():
    global photo3
    photo3 = PhotoImage(file="Rock.png")
    can.create_image(0,0, anchor = NW, image=photo3)
    can.pack(side=TOP, padx=5, pady=5)

def P_paper():
    global photo3
    photo3 = PhotoImage(file="Paper.png")
    can.create_image(0,0, anchor = NW, image=photo3)
    can.pack(side=TOP, padx=5, pady=5)

def P_scissors():
    global photo3
    photo3 = PhotoImage(file="Scissors.png")
    can.create_image(0,0, anchor = NW, image=photo3)
    can.pack(side=TOP, padx=5, pady=5)

def P_lizard():
    global photo3
    photo3 = PhotoImage(file="Lizard.png")
    can.create_image(0,0, anchor = NW, image=photo3)
    can.pack(side=TOP, padx=5, pady=5)

def P_spock():
    global photo3
    photo3 = PhotoImage(file="Spock.png")
    can.create_image(0,0, anchor = NW, image=photo3)
    can.pack(side=TOP, padx=5, pady=5)

#Image pour l'IA
    
def AI_rock():
    global photo4
    photo4 = PhotoImage(file="Rock.png")
    can.create_image(350,250, anchor = NW, image=photo4)
    can.pack(side=TOP, padx=5, pady=5)

def AI_paper():
    global photo4
    photo4 = PhotoImage(file="Paper.png")
    can.create_image(350,250, anchor = NW, image=photo4)
    can.pack(side=TOP, padx=5, pady=5)

def AI_scissors():
    global photo4
    photo4 = PhotoImage(file="Scissors.png")
    can.create_image(350,250, anchor = NW, image=photo4)
    can.pack(side=TOP, padx=5, pady=5)

def AI_lizard():
    global photo4
    photo4 = PhotoImage(file="Lizard.png")
    can.create_image(350,250, anchor = NW, image=photo4)
    can.pack(side=TOP, padx=5, pady=5)

def AI_spock():
    global photo4
    photo4 = PhotoImage(file="Spock.png")
    can.create_image(350,250, anchor = NW, image=photo4)
    can.pack(side=TOP, padx=5, pady=5)   

fenetre= Tk()

frame_rulesandplay = Frame(fenetre, relief=GROOVE)
frame_rulesandplay.pack(side=TOP)

def display_rules():
    can.delete("all")
    global sheldon
    global rules
    sheldon = PhotoImage(file="Sheldon.png")
    can.create_image(0,200, anchor = NW, image=sheldon)
    rules = PhotoImage(file="Rules.png")
    can.create_image(150,0, anchor = NW, image=rules)
buton_rules = Button(frame_rulesandplay, text="Rules", command=display_rules)
buton_rules.pack(side=LEFT, padx=8, pady=8)

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
buton_go = Button(frame_rulesandplay, text="Play", command=go)
buton_go.pack(side=LEFT, padx=8, pady=8)

can= Canvas(fenetre, width=500, height=400, bg='white')

photo = PhotoImage(file="B1.png")
photo2 = PhotoImage(file="Base.png")
AI = PhotoImage(file="IA.png")
can.create_image(0,300, anchor = NW, image=photo2)
can.create_image(300,0, anchor = NW, image=AI)
can.create_image(0,300, anchor = NW, image=photo)
can.pack(side=TOP, padx=5, pady=5)


Frame_buttons = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame_buttons.pack()
# frame 1 dans fenetre
Frame1 = Frame(Frame_buttons, bg="yellow", borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=5, pady=1)

# Ajout de boutons + label, dans frame1
Label(Frame1, bg = "yellow", text="Moves").pack(pady=1)
b1=Button(Frame1, text ="Rock\n(press x)", command=touche_pressed)
b2=Button(Frame1, text ='Paper\n(press c)', command=touche_pressed)
b3=Button(Frame1, text ='Cisors\n(press v)', command=touche_pressed)
b4=Button(Frame1, text ='Lizard\n(press b)', command=touche_pressed)
b5=Button(Frame1, text ='Spock\n(press n)', command=touche_pressed)
b1.pack(side=LEFT, padx=8, pady=8)
b2.pack(side=LEFT, padx=8, pady=8)
b3.pack(side=LEFT, padx=8, pady=8)
b4.pack(side=LEFT, padx=8, pady=8)
b5.pack(side=LEFT, padx=8, pady=8, )

#Frame2 dans la fenêtre + ajout d'un bouton quitter et replay dans cette frame
Frame2 = Frame(Frame_buttons, relief=GROOVE)
Frame2.pack(side=RIGHT, padx=5, pady=1)
Label(Frame2, text="Fonctions").pack(pady=1)
def replay():
    go()
    global p1
    p1 = 0
    global p2 
    p2 = 0
buton_replay=Button(Frame2, text="Replay", command=replay)
buton_replay.pack(side=LEFT, padx=15, pady=8)
buton_quit=Button(Frame2, text="Exit", command=quit)
buton_quit.pack(side=LEFT, padx=8, pady=8)
def quit():
    fenetre.destroy
    sys.exit("Error message")

#Frame 3 dans la fenêtre. Relate des résultats du game
Frame3 = Frame(fenetre, bg="blue", relief=GROOVE)
Frame3.pack(side=BOTTOM, pady=20)

label_results = Label(Frame3, text="texte")

#win/loose message
def victory():
    if askyesno('Victory !', 'You won !\nWant to play again ?'):
        replay()
    else:
        quit()
def defeat():
    if askyesno('Defeat !', 'You loose :(\nWant to play again ?'):
        replay()
    else:
        quit()

#fenetre pour rentrer son nom
def displayText():
    global entryWidget
    global name
    name = entryWidget.get().strip()
    root.destroy()
    fenetre.attributes("-topmost", True)
    
if __name__ == "__main__":

    root = Tk()

    root.title("Who are you ?")
    root["padx"] = 40
    root["pady"] = 20   
    root.attributes("-topmost", True)

    # Create a text frame to hold the text Label and the Entry widget
    textFrame = Frame(root)

    #Create a Label in textFrame
    entryLabel = Label(textFrame)
    entryLabel["text"] = "Please state your name"
    entryLabel.pack(side=LEFT)

    # Create an Entry Widget in textFrame
    entryWidget = Entry(textFrame)
    entryWidget["width"] = 20
    entryWidget.pack(side=LEFT)

    textFrame.pack()

    button_submit = Button(root, text="Submit", command=displayText)
    button_submit.pack()

fenetre.mainloop()
while p1 <= 2 or p2 <= 2:
    touche_pressed()
