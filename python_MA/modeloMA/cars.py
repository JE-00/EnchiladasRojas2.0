import agentpy as ap
import random


class Car(ap.Agent):
    def setup(self):
        self.grid = self.grid
        self.pos = self.grid.pos[self]
        self.pos_x = self.pos[0]
        self.pos_z = self.pos[1]
        self.mass = random.randint(1, 10)
        self.type = random.randint(0, 3)
        # self.velocity = normalize()
        self.direction = random.randint(0, 3)
        self.max_speed = 3
        self.car_separation = 0.1
        self.state = 0

        self.print_data()

    def print_data(self):
        print("Car:\nmass: ", self.mass, "type: ", self.type, "direction: ", self.direction)

    def get_pos(self):
        self.pos = self.grid.positions[self]
        self.pos_x = self.pos[0]
        self.pos_z = self.pos[1]

    def move(self):
        self.state = 1
        if (self.direction == 0) : self.pos_x += 1
        elif (self.direction == 1) : self.pos_z += 1
        elif (self.direction == 2) : self.pos_x -= 1
        elif (self.direction == 3) : self.pos_z -= 1

    def stop(self):
        self.state = 0
