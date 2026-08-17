class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted([(position[i], speed[i], (target-position[i])/speed[i]) for i in range(n)], key = lambda c: c[0], reverse = True)
        fleets = []
        for position, speed, time_to_target in cars:
            if fleets and fleets[-1][2] < time_to_target:
                fleets.append((position, speed, time_to_target))
            elif not fleets:
                fleets.append((position, speed, time_to_target))
        
        return len(fleets)
