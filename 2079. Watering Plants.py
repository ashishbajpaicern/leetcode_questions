class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        bucket = capacity
        for i in range(len(plants)):
            steps += 1
            if plants[i] > bucket:
                steps += 2 * i
                bucket = capacity - plants[i]
                continue
            bucket -= plants[i]
        return steps
