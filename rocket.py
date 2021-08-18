import random
from math import sqrt

class Rocket:

    def __init__(self, id, speed, altitude=0, x=0):
        self.altitude = altitude
        self.x = x
        self.id = id
        self.speed = speed


    def moveUp(self):
        """ this function will move up with speed
        """
        self.altitude += self.speed


    def __str__(self):
        return 'Rocket ' + str(self.id) + ' have coordinates: (' + str(self.altitude) + ',' + str(self.x) + ')'


    def get_distance(self, rocket):
        ab = rocket.altitude - self.altitude
        bc = rocket.x - self.x
        distance = sqrt(ab**2 + bc**2)
        return distance

class RocketBoard:

    def __init__(self, amountOfRockets = 5):
        speeds = [random.randint(1,5) for _ in range(amountOfRockets)]
        self.rockets = [Rocket(id, speeds[id]) for id in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = random.randint(0,amountOfRockets-1)
            self.rockets[rocketIndexToMove].moveUp()
        
        for rocket in self.rockets:
            print(rocket)


    def __getitem__(self, key):
        return self.rockets[key]


    def __setitem__(self, key, value):
        self.rockets[key].altitude = value