import agentpy as ap
import random


class People(ap.Agent):

    def setup(self):
        self.mass = random.randint(1, 5)
        self.direction = random.randint(0, 3) # 0 - 3 = Arriba a Izquierda clockwise
        self.max_speed = 1

        self.print_data()
        self.move()

    def print_data(self):
        print("People:\nmass: ", self.mass, "direction: ", self.direction)

    def move(self):
        pass
