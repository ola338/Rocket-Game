import random
from math import sqrt


class Rocket:

    def __init__(self, id, speed, altitude=0, x=0):
        self.altitude = altitude
        self.x = x
        self.id = id
        self.speed = speed


    def moveUp(self):
        self.altitude += self.speed


    def __str__(self):
        return 'Rocket ' + str(self.id) + ' have coordinates: (' + str(self.altitude) + ',' + str(self.x) + ')'


    def get_distance(self, rocket):
        ab = rocket.altitude - self.altitude
        bc = rocket.x - self.x
        distance = sqrt(ab**2 + bc**2)
        return distance


class RocketBoard:

    def __init__(self, altitude, x, amountOfRockets = 5):
        self.amountOfRockets = amountOfRockets
        speeds = [random.randint(1,5) for _ in range(amountOfRockets)]
        self.rockets = [Rocket(id, speeds[id], altitude, x) for id in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = random.randint(0,amountOfRockets-1)
            self.rockets[rocketIndexToMove].moveUp()
        
        for rocket in self.rockets:
            print(rocket)


    def __getitem__(self, key):
        return self.rockets[key]


    def get_max_distance(self):
        maxDistance = 0.0
        for i in range(self.amountOfRockets):
            for j in range(self.amountOfRockets):
                distance = self.rockets[i].get_distance(self.rockets[j])
                if distance > maxDistance:
                    maxDistance = distance   
        return maxDistance


    def get_min_distance(self):
        minDistance = self.rockets[0].get_distance(self.rockets[1])
        for i in range(self.amountOfRockets):
            for j in range(self.amountOfRockets):
                if i == j:
                    continue
                else:
                    distance = self.rockets[i].get_distance(self.rockets[j])
                    if distance < minDistance:
                        minDistance = distance   
        return minDistance




    #def __setitem__(self, key, value):
     #   self.rockets[key].altitude = value

    
