#---------- Read me -----------
"""
interface créée durant le confinement de mars 2020 par Arnaud de Kanker
fait en 4 jours

pour rajouter une condition homo et sa valeur, il suffit de l'ajouter dans le 'dicoche' en bas
"""
#--------- background ---------
from tkinter import *
from tkinter import ttk
diconame = {'a' : 19, 'b' : 32, 'c': 9598, 'd': 32, 'e': 64, 'f': 80, 'g' : 42, 'h' : 28, 'i' : 36, 'j': 74, 'k' : 89,
'l' : 64, 'm': 48 , 'n' : 74, 'o' : 29, 'p' : 56, 'q': 853989, 'r' : 45, 's' : 73, 't' : 49, 'u' : 36, 'v' : 79, 'w': 994, 'x' : 727,
'y' : 59, 'z': 94, 'é' : 56, 'è' : 23, ' ' : 23, '-' : 10}

dicoche = {
"Tu viens de Maredsous" : -100,
"Tu viens de Saint-Michel" : 14867,
"Tu fais pipi assis" : 50,
"Tu as deja fait les prelis avec quelqu'un du même sexe" :5078,
"Tu es homo" : 299792458,
"Tu as déjà embrassé quelqu'un du meme sexe" : 78,
"Tu as un plaisir prostatique (homme)" : 140,
"Tu fumes des lime" : 70,
"Tu as un Iphone" :-100,
"Tu t'essuies la teub après avoir pissé" : 50,
"Tu as déjà bu une summersby" : 68,
"Tu prend des tacos sans sauce fromagère " : 60,
"Tu portes des slims" : 86,
"Tu bois du coca sans sucre" : 67,
"Tu utilises des smileys (:-),x))": 70,
"Tu es de gauche": 679,
"Tu as une ceinture off white":420,
"Tu fais des sudoku": 43,
"Tu manges parfois exki" : 80,
"Tu fais de l'art ( peinture photo etc)": 30,
"Tu es en fac de littérature ": 739,
"Tu manges Bio": 30,
"Tu bois de la sangria en soirée": 47,
"Tu portes des lunettes " : 47,
"Tu prends de l'homéopathie" : 554,
"Tu as des cheveux de couleur artificielle": 7409,
"Tu as un piercing": 4895,
"Tu passes le confinement avec un ''ami''" : 598,
"Tu suces des bites": 446,
"Tu écoutes Angèle fréquemment":50,
"Tu dis #noHomo": 157,
"Tu dis hihi / xd oralement" : 146,
"Tu portes une écharpe": 80
}

liste_dicoKeys =[]

for item in dicoche.keys():
    liste_dicoKeys.append(item)

listecoche = []

def getvalues():
    l = 0
    count2 = 0

    naam = nom.get()
    name = prenom.get() + naam
    l += 6*len(naam.split())

    for i in name.lower():
        l += (diconame[i])
    l2 = l

    for naets in listecoche:
        if naets.get() == 1:
            l += dicoche.get(liste_dicoKeys[count2])
        count2 += 1


    if  l < 1000:
        gayvalue = '0' 
        heterovalue = '100'
        remarque = "C'est ok!"
    if l >= 1000 :
        gayvalue = '25'
        heterovalue = '75'
        remarque = 'Prudence !'
    if l >= 4000 :
        gayvalue = '50'
        heterovalue = '50'
        remarque = 'Resaisis toi !!!!'
    if l >= 10000 :
        gayvalue = '75'
        heterovalue = '25'
        remarque = 'TU DÉCONNES ?!'
    if l >= 15000 :
        gayvalue = '100'
        heterovalue = '0'
        remarque = 'On ne peut plus rien pour toi.'

    valeur.config ( text = (' Tu as ' +str(l)+' points homo (dont '+ str(l2)+' à cause de ton nom)'), font = ('Times new roman', 15) )
    valeur2.config( text = ('Tu es donc hétéro à {0} % et gay à {1} %. {2}'.format(heterovalue,gayvalue,remarque)),font = ('Times new roman', 20))

#---------- interface ---------
window = Tk()
boutons = Canvas(window, bg = '#CDCDCD', highlightthickness = 0)
inpute  = Canvas(window, bg = '#CDCDCD', highlightthickness = 0)
coche   = Canvas(window, bg = '#CDCDCD', highlightthickness = 0)


window.title("Test si t'es homo")
window.geometry('2000x1500')
window.minsize(1080,720)

window.config(background='#CDCDCD')

#---------- elements -----------
titre = Label(window, text = 'Bonjour et bienvenue dans ce test',font=('Times new roman',70,'bold', 'underline', 'italic'),bg = '#CDCDCD')
soustitre = Label(window,text = 'Grace à ce test, vous allez enfin savoir si vous êtes homosexuel !!!', font = ('Times new roman', 30), bg = '#CDCDCD')
explain = Label(window, text = 'Inscrivez votre nom et prénom et cochez les cases qui correspondent à votre attitude', font = ('Times new roman', 20), bg = '#CDCDCD')

label_nom = Label(inpute, text = 'Nom', font = ('Times new roman', 15), bg = '#CDCDCD')
label_prenom = Label(inpute, text = 'Prénom', font = ('Times new roman', 15), bg = '#CDCDCD')
prenom = Entry(inpute, bg = '#CDCDCD', highlightthickness = 0)
nom = Entry(inpute, bg = '#CDCDCD', highlightthickness = 0)

valider = Button(boutons,text = 'Valider', command = getvalues, highlightbackground="#CDCDCD", fg="Black", highlightthickness=0)
quitter = Button(boutons, text = 'Quitter', command= window.quit, bg = '#CDCDCD', highlightbackground="#CDCDCD", fg="Black", highlightthickness=0, relief = 'flat')
valeur  = Label(window,bg = '#CDCDCD')
valeur2 = Label(window,bg = '#CDCDCD')

#--------- Packing ----------

titre.pack()
soustitre.pack()
explain.pack()
inpute.pack(pady = 20)

label_prenom.grid(row = 0, column = 0 )
prenom.grid(row = 0, column = 1)
label_nom.grid(row = 1, column = 0)
nom.grid(row = 1, column = 1)
#--- pack des trucs à cocher 
coche.pack()

count = 0
for texte in dicoche.keys():
    var = IntVar()
    Checkbutton(coche, text = texte, bg = '#CDCDCD', font = ('Times new roman', 15) ,highlightthickness = 0, variable = var).grid(row = count//2, column = count%2,padx = 100,sticky = W)
    listecoche.append(var)
    count += 1

boutons.pack(pady = 10)
valider.grid(row = 0, column = 0, padx = 30)
quitter.grid(row = 0, column = 2, padx = 30)
valeur.pack()
valeur2.pack()
window.mainloop()
