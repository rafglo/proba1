import zad4lista6 as kip
import random
from zad1lista7 import Rocket
import matplotlib.pyplot as plt
rakiety = []
while(len(rakiety)) < 5:
    rakieta = (random.uniform(-10,10), random.uniform(-10,10), 0)
    ile = 0
    for rakieta1 in rakiety:
        if kip.kolizja(rakieta, rakieta1):
            ile += 1
    if ile == 0:
        rakiety.append(rakieta)


r1 = Rocket("r1", 10, rakiety[0][0], rakiety[0][1])
r2 = Rocket("r2", 10, rakiety[1][0], rakiety[1][1])
r3 = Rocket("r3", 10, rakiety[2][0], rakiety[2][1])
r4 = Rocket("r4", 10, rakiety[3][0], rakiety[3][1])
r5 = Rocket("r5", 10, rakiety[4][0], rakiety[4][1])

rakiety_nowe = []
rakiety_nowe.append(r1)
rakiety_nowe.append(r2)
rakiety_nowe.append(r3)
rakiety_nowe.append(r4)
rakiety_nowe.append(r5)

print("Pozycja początkowa rakiety pierwszej: ("+ str(rakiety_nowe[0].x) + ", " + str(rakiety_nowe[0].y) + ")")
print("Pozycja początkowa rakiety drugiej: (" + str(rakiety_nowe[1].x) + ", " + str(rakiety_nowe[1].y) + ")")
print("Pozycja początkowa rakiety trzeciej: (" + str(rakiety_nowe[2].x) + ", " + str(rakiety_nowe[2].y) + ")")
print("Pozycja początkowa rakiety czwartej: (" + str(rakiety_nowe[3].x) + ", " + str(rakiety_nowe[3].y) + ")")
print("Pozycja początkowa rakiety piątej: (" + str(rakiety_nowe[4].x) + ", " + str(rakiety_nowe[4].y) + ")")
print("Odległości początkowe: ")
print("1 -> 2 : " + str(rakiety_nowe[0].get_distance(rakiety_nowe[1])[0]))
print("1 -> 3 : " + str(rakiety_nowe[0].get_distance(rakiety_nowe[2])[0]))
print("1 -> 4 : " + str(rakiety_nowe[0].get_distance(rakiety_nowe[3])[0]))
print("1 -> 5 : " + str(rakiety_nowe[0].get_distance(rakiety_nowe[4])[0]))
print("2 -> 3 : " + str(rakiety_nowe[1].get_distance(rakiety_nowe[2])[0]))
print("2 -> 4 : " + str(rakiety_nowe[1].get_distance(rakiety_nowe[3])[0]))
print("2 -> 5 : " + str(rakiety_nowe[1].get_distance(rakiety_nowe[4])[0]))
print("3 -> 4 : " + str(rakiety_nowe[2].get_distance(rakiety_nowe[3])[0]))
print("3 -> 5 : " + str(rakiety_nowe[2].get_distance(rakiety_nowe[4])[0]))
print("4 -> 5 : " + str(rakiety_nowe[3].get_distance(rakiety_nowe[4])[0]))

plt.axis([-11,11,-11,11])
wsp_x = []
wsp_y =[]
kolory = ["red", "blue", "green", "yellow", "orange"]
rakiety_nazwy = ["rakieta nr 1", "rakieta nr 2", "rakieta nr 3", "rakieta nr 4", "rakieta nr 5"]
for rakieta in rakiety_nowe:
    plt.scatter(rakieta.x, rakieta.y)
plt.legend(rakiety_nazwy, loc = 'best')
plt.show()

czy_dalej = True
while czy_dalej:
    plt.clf()
    ktora_rakieta = input("Podaj numer rakiety, którą chcesz przesunąć, jeśli chcesz skończyć napisz 'stop'")
    if ktora_rakieta == 'stop':
        czy_dalej = False
    else:
        if 1 <= int(ktora_rakieta) <= 5:
            dx = int(input("Podaj, o ile chcesz przesunąć rakietę nr " + str(ktora_rakieta) + " wzdłuż osi OX"))
            dy = int(input("Podaj, o ile chcesz przesunąć rakietę nr " + str(ktora_rakieta) + " wzdłuż osi OY"))
            while not(-10 <= rakiety_nowe[int(ktora_rakieta) - 1].x + dx <= 10 and -10 <= rakiety_nowe[int(ktora_rakieta) - 1].y + dy <= 10):
                dx = int(input("Wyszedłeś poza planszę! Podaj jeszcze raz, o ile chcesz przesunąć rakietę nr " + str(ktora_rakieta) + " wzdłuż osi OX"))
                dy = int(input("Podaj jeszcze raz, o ile chcesz przesunąć rakietę nr " + str(ktora_rakieta) + " wzdłuż osi OY"))
            else:
                rakiety_nowe[int(ktora_rakieta) - 1].move(dx, dy)
                print("Pozycja rakiety pierwszej: ("+ str(rakiety_nowe[0].x) + ", " + str(rakiety_nowe[0].y) + ")")
                print("Pozycja rakiety drugiej: (" + str(rakiety_nowe[1].x) + ", " + str(rakiety_nowe[1].y) + ")")
                print("Pozycja rakiety trzeciej: (" + str(rakiety_nowe[2].x) + ", " + str(rakiety_nowe[2].y) + ")")
                print("Pozycja rakiety czwartej: (" + str(rakiety_nowe[3].x) + ", " + str(rakiety_nowe[3].y) + ")")
                print("Pozycja rakiety piątej: (" + str(rakiety_nowe[4].x) + ", " + str(rakiety_nowe[4].y) + ")")
                print("Odległości: ")
                print("1 -> 2 : " + str(rakiety_nowe[0].get_distance(rakiety_nowe[1])[0]))
                print("1 -> 3 : " + str(rakiety_nowe[0].get_distance(rakiety_nowe[2])[0]))
                print("1 -> 4 : " + str(rakiety_nowe[0].get_distance(rakiety_nowe[3])[0]))
                print("1 -> 5 : " + str(rakiety_nowe[0].get_distance(rakiety_nowe[4])[0]))
                print("2 -> 3 : " + str(rakiety_nowe[1].get_distance(rakiety_nowe[2])[0]))
                print("2 -> 4 : " + str(rakiety_nowe[1].get_distance(rakiety_nowe[3])[0]))
                print("2 -> 5 : " + str(rakiety_nowe[1].get_distance(rakiety_nowe[4])[0]))
                print("3 -> 4 : " + str(rakiety_nowe[2].get_distance(rakiety_nowe[3])[0]))
                print("3 -> 5 : " + str(rakiety_nowe[2].get_distance(rakiety_nowe[4])[0]))
                print("4 -> 5 : " + str(rakiety_nowe[3].get_distance(rakiety_nowe[4])[0]))
                plt.axis([-11, 11, -11, 11])
                wsp_x = []
                wsp_y = []
                kolory = ["red", "blue", "green", "yellow", "orange"]
                rakiety_nazwy = ["rakieta nr 1", "rakieta nr 2", "rakieta nr 3", "rakieta nr 4", "rakieta nr 5"]
                for rakieta in rakiety_nowe:
                    plt.scatter(rakieta.x, rakieta.y)
                plt.legend(rakiety_nazwy, loc='best')
                plt.show()

        else:
            print("Nie ma takiej rakiety, podaj jeszcze raz")
            continue



