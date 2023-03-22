from zad1lista7 import Rocket
import random

rakieta = Rocket("r1")
for i in range(5):
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    rakieta.move(x,y)
    pozycja = rakieta.get_position()
    print(pozycja)