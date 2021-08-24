from __future__ import annotations
import random
from math import sqrt


class Rocket:
    
    id = 0

    def __init__(self, speed: float, altitude: float = 0, position: float = 0):
        self.altitude = altitude
        self.position = position
        self.speed = speed
        self.id = Rocket.id
        Rocket.id += 1

    def move(self):
        '''
        This method move rocket up and sideways according to the speed

        '''
        self.altitude += self.speed
        self.position += self.speed/2


    def __str__(self):
        return 'Rocket ' + str(self.id + 1) + ' have speed: ' + str(self.speed) + ' and coordinates: (' + str(self.altitude) + ',' + str(self.position) + ')'


    def get_distance(self, rocket: Rocket) -> float:
        '''
        This method give the distance between 2 rocket

        '''
        ab = rocket.altitude - self.altitude
        bc = rocket.position - self.position
        distance = sqrt(ab**2 + bc**2)
        return distance
    

class RocketBoard:

    def __init__(self, initAltitude: float, initPosition: float, amountOfRockets: int = 5):
        self.initAltitude = initAltitude
        self.initPosition = initPosition
        self.amountOfRockets = amountOfRockets
        self.speeds = [random.randint(1,5) for _ in range(amountOfRockets)]
        self.rockets = [Rocket(self.speeds[id], initAltitude, initPosition) for id in range(amountOfRockets)]

        for _ in range(10):
            rocketIndexToMove = random.randint(0, amountOfRockets-1)
            self.rockets[rocketIndexToMove].move()   # move random rocket
        
        for rocket in self.rockets:
            print(rocket)


    def __getitem__(self, key):
        return self.rockets[key]


    def __len__(self):
        return len(self.rockets)


    def get_max_distance(self) -> float:
        '''
        This method give the maximum distance between 2 rocket

        '''
        maxDistance = 0.0
        for i in range(self.amountOfRockets):
            for j in range(self.amountOfRockets):
                distance = self.rockets[i].get_distance(self.rockets[j])
                if distance > maxDistance:
                    maxDistance = distance   
        return maxDistance


    def get_min_distance(self) -> float:
        '''
        This method give the minimum distance between 2 rocket

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


    def get_ranking(self) -> dict:
        '''
        This method give ranking of rockets depending of speed
        '''            
        sortedSpeeds = self.speeds.copy()
        sortedSpeeds.sort(reverse=True)
        sortedSpeeds = list(dict.fromkeys(sortedSpeeds))   # remove duplicates
        ranking = {}
        for i in range(self.amountOfRockets):
            speedOfRocket = self.speeds[i]
            rank = sortedSpeeds.index(speedOfRocket)
            ranking[i+1] = rank + 1
        return ranking


    def get_fastest_rockets(self) -> list:
        '''
        This method give list of the fastest rocket

        '''        
        keys = list(self.get_ranking().keys())
        values = list(self.get_ranking().values())
        theBestRank = min(values)
        amountOfSlowestRockets = values.count(theBestRank)
        FastestRocket = list()
        for _ in range(amountOfSlowestRockets):
            FastestRocket.append(keys[values.index(theBestRank)])
            values[values.index(theBestRank)] = 0
        return FastestRocket


    def get_slowest_rockets(self) -> list:
        '''
        This method give list of the slowest rocket

        '''
        keys = list(self.get_ranking().keys())
        values = list(self.get_ranking().values())
        theLatestRank = max(values)
        amountOfSlowestRockets = values.count(theLatestRank)
        SlowestRocket = list()
        for _ in range(amountOfSlowestRockets):
            SlowestRocket.append(keys[values.index(theLatestRank)])
            values[values.index(theLatestRank)] = 0
        return SlowestRocket


    def get_distance_ranking(self) -> dict:
        '''
        This method give ranking of rockets depending of distance
        '''   
        distances = {}
        for rocketId in range(self.amountOfRockets):
            ab = self.initAltitude - self.rockets[rocketId].altitude
            bc = self.initPosition - self.rockets[rocketId].position
            totalDistance = sqrt(ab**2 + bc**2)
            distances[rocketId+1] = totalDistance
        return distances
        

    def get_the_weakest_rockets(self) -> list:
        '''
        This method give list of rocket which travelled the shortest distance

        '''        
        keys = list(self.get_distance_ranking().keys())
        values = list(self.get_distance_ranking().values())
        minDistance = min(values)
        amountOfWeakestRockets = values.count(minDistance)
        weakestRocket = list()
        for _ in range(amountOfWeakestRockets):
            weakestRocket.append(keys[values.index(minDistance)])
            values[values.index(minDistance)] = -1
        return weakestRocket


    def get_the_best_rockets(self) -> list:
        '''
        This method give list of rocket which travelled the longest distance

        '''        
        keys = list(self.get_distance_ranking().keys())
        values = list(self.get_distance_ranking().values())
        maxDistance = max(values)
        amountOfWeakestRockets = values.count(maxDistance)
        bestRocket = list()
        for _ in range(amountOfWeakestRockets):
            bestRocket.append(keys[values.index(maxDistance)])
            values[values.index(maxDistance)] = -1
        return bestRocket
