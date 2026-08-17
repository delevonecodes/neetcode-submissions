class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted([(position[i], (target-position[i])/speed[i]) for i in range(n)], key = lambda c: c[0], reverse = True)
        fleets = []
        for position, time_to_target in cars:
            if fleets and fleets[-1][1] < time_to_target:
                fleets.append((position, time_to_target))
            elif not fleets:
                fleets.append((position, time_to_target))
        
        return len(fleets)
