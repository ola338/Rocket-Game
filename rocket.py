import random

class Rocket:
    def __init__(self, number, speed):
        self.altitude = 0
        self.number = number
        self.speed = speed

    def moveUp(self):
        """ this function will move up with speed
        """
        self.altitude += self.speed

    def __str__(self):
        return 'Rocket ' + str(self.number) + ' have altitude: ' + str(self.altitude)


class RocketBoard:
    def __init__(self, amountOfRockets = 5):
        speeds = [random.randint(1,5) for _ in range(amountOfRockets)]
        self.rockets = [Rocket(i, speeds[i]) for i in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = random.randint(0,amountOfRockets-1)
            self.rockets[rocketIndexToMove].moveUp()
        
        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key):
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value