from modeloMA.model import Model
import time


parameters = {
    "size": 50,
    "ndim": 2,
    "num_of_lights": 2,
    "num_of_cars": 10,
    "num_of_people": 2,
    "car_separation": 0.1
}

env = Model(parameters)
env.setup()

while True:
    time.sleep(1)
    env.step()
    # env.update()
