class Solution:
    def carFleet(self, target:int, position:List[int], speed:List[int]) -> int:
        cars = list(zip(position, speed))

        cars.sort(reverse=True)
        
        fleets = 0
        fleet_time = 0

        for pos, spd in cars:
            arrival_time = (target - pos) / spd
            if arrival_time > fleet_time:
                fleets += 1
                fleet_time = arrival_time
        
        return fleets