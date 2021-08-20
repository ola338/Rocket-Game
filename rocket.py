import random
from math import sqrt


class Rocket:

    def __init__(self, id, speed, altitude=0, position=0):
        self.altitude = altitude
        self.position = position
        self.id = id
        self.speed = speed


    def move(self):
        '''
        This function move rocket up and sideways according to the speed

        '''
        self.altitude += self.speed
        self.position += self.speed/2


    def __str__(self):
        return 'Rocket ' + str(self.id + 1) + ' have coordinates: (' + str(self.altitude) + ',' + str(self.position) + ')'


    def get_distance(self, rocket):
        '''
        This function give the distance between 2 rocket

        '''
        ab = rocket.altitude - self.altitude
        bc = rocket.position - self.position
        distance = sqrt(ab**2 + bc**2)
        return distance


class RocketBoard:

    def __init__(self, altitude, position, amountOfRockets = 5):
        self.amountOfRockets = amountOfRockets
        self.speeds = [random.randint(1,5) for _ in range(amountOfRockets)]
        self.rockets = [Rocket(id, self.speeds[id], altitude, position) for id in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = random.randint(0, amountOfRockets-1)
            self.rockets[rocketIndexToMove].move()   # move random rocket
        
        for rocket in self.rockets:
            print(rocket)


    def __getitem__(self, key):
        return self.rockets[key]


    def get_max_distance(self):
        '''
        This function give the maximum distance between 2 rocket

        '''
        maxDistance = 0.0
        for i in range(self.amountOfRockets):
            for j in range(self.amountOfRockets):
                distance = self.rockets[i].get_distance(self.rockets[j])
                if distance > maxDistance:
                    maxDistance = distance   
        return maxDistance


    def get_min_distance(self):
        '''
        This function give the minimum distance between 2 rocket

        '''
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


    def get_ranking(self):
        sortedSpeeds = self.speeds
        sortedSpeeds.sort(reverse=True)
        sortedSpeeds = list(dict.fromkeys(sortedSpeeds))   # remove duplicates
        ranking = {}
        for i in range(self.amountOfRockets):
            speedOfRocket = self.speeds[i]
            rank = sortedSpeeds.index(speedOfRocket)
            ranking[i+1] = rank + 1
        return sortedSpeeds, ranking

    
    def get_fastest_rocket(self):
        return 

    
