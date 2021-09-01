import agentpy as ap
import time


class TLights(ap.Agent):

    def setup(self):
        self.state = 0
        self.car_count = 0
        self.car_limit = 10
        self.wait_time = 30
        self.last_update = time.time()

        #self.setup_pos(grid)
        self.get_car_count()

    def setup_pos(self, grid: ap.Grid):
        self.grid = grid
        self.pos = grid.positions[self]


    def update(self):
        self.state += 1
        if self.state > 2:
            self.state = 0
        self.wait_time = 30
        self.last_update = time.time()

    def set_wait_time(self):
        if self.get_state() == 2 and self.get_car_count() >= self.car_limit:
            self.wait_time *= 2
        else: self.wait_time = 30

    def get_state(self):
        if self.last_update - time.time() > self.wait_time:
            self.update()
        return self.state

    def add_car_count(self):
        self.car_count += 1

    def remove_car_count(self):
        if self.car_count > 0:
            self.car_count -= 1

    def get_car_count(self):
        return self.car_count

    def print_data(self):
        print("Traffic Light:\nColor: ", self.state, "Car count: ", self.car_count, "Wait time: ", self.wait_time)
