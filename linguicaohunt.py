#-------------------------------#
#  WELCOME TO LINGUIHUNT! #
#-------------------------------#

from turtle import *
from random import *
from time import *

#FUNCAO DOS CLIQUES
def cliques(x,y):
    print(pos()[0])
    print(pos()[1])

    if pos()[0]+20 > x and pos()[0]-20 < x and pos()[1]+20 > y and pos()[1]-20 <y:
        print("acertou")
        global acertos
        acertos = acertos + 1
        penup()
        goto(250,250)
        clear()
        write("Acertos: " + str(acertos), move=False, align="center", font=("Arial", 16, "normal"))
        linguicas()

    print('mouse clicked at (' + str(x) + ', ' + str(y) + ')')

def linguicas ():
    global ultimaatualiza
    ultimaatualiza=time()
    penup()
    if acertos == 0:
        goto(250, 250)
        write("Acertos: 0", move=False, align="center", font=("Calibri", 16, "normal"))

    x = randint (-300,300)
    y = randint (-200,200)
    
    goto(x,y)
    pendown()

    if acertos == 10:
        printgameover()
        clear()
        hideturtle()

def tempos ():
    global ultimaatualiza
    if time() - ultimaatualiza > 0.7:
        linguicas()
    
    ontimer(tempos, 100) #Serve como um loop infinito, chama a funcao a cada 100milisegundos

def printgameover():
    global gameover
    if not gameover:
        a = Turtle()
        a.speed(0)
        a.hideturtle()
        a.penup()
        a.goto(-200, -30)
        a.write("THE CAOS HAS ENDED!", font=("Calibri", 30, "normal"))
        gameover = True
        
def printinicio():
    global tartarugaInicio
    tartarugaInicio = Turtle()
    tartarugaInicio.speed(0)
    tartarugaInicio.hideturtle()
    tartarugaInicio.penup()
    tartarugaInicio.goto(-250, -30)
    tartarugaInicio.write("THE CAOS STARTS IN 3...2...1!", font=("Calibri", 30, "normal"))
    ontimer(start,4000)

#  ***** FUNCAO PRINCIPAL  *****  #
#BACKGROUND      
delay(0)
setup(800,600)
bgcolor("yellow")

#SHAPE LINGUICAS 
register_shape("linguicaredimens.gif")
shape("linguicaredimens.gif")
ht()

#VARIAVEIS
acertos = 0
atualiza = time()
ultimaatualiza = atualiza
gameover =  False
tartarugaInicio = False

#CHAMADAS DE FUNCAO
def start():
    tartarugaInicio.clear()
    showturtle()
    linguicas()
    onclick(cliques)
    speed(0)
    ontimer(tempos, 500)

printinicio()
mainloop()
