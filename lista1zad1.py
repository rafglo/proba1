import random

class Vector:

    def __init__(self, args = 3):
        self.wektor = []
        for i in range(args):
            self.wektor.append(0)
    
    def losowanie(self):
        for i in range(len(self.wektor)):
            self.wektor[i] = random.randint(0,10)
            

