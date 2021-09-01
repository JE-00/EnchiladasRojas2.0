import agentpy as ap
from agentpy.grid import Grid
from modeloMA.cars import Car
from modeloMA.tLights import TLights
from modeloMA.people import People
import numpy as np
import random

class Model(ap.Model):
    def setup(self):
        self.matrix = np.zeros((self.p.size, self.p.size))

        self.lights = ap.AgentList(self, self.p.num_of_lights, TLights)
        self.cars = ap.AgentList(self, self.p.num_of_cars, Car)
        self.people = ap.AgentList(self, self.p.num_of_people, People)

        self.grid = Grid(self, (self.p.size, self.p.size), track_empty=True)
        self.grid.add_agents(self.cars, positions= [(0,24), (24, 0), (25, 49), (49, 25)], random=True, empty=True)
        """ self.grid.add_agents(self.people, random=True, empty=True)
        self.grid.add_agents(self.lights, random=True, empty=True) """


        #agents.setup_pos <--esto x 3

    def step(self):
        for light in self.lights:
            light.get_state()
            light.print_data()

        for car in self.cars:
            car.print_data()
            light.add_car_count()

        for person in self.people:
            person.print_data()


    def update(self):
        for light in self.lights:
            light.get_state()

    def end(self):
        self.lights.record('num_of_cars')
        self.cars.record('pos')
        self.people.record('pos')
