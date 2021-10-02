class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        res = [-1] * len(workers)
        taken_bikes = set()
        distances = collections.defaultdict(list)
        for i, bike in enumerate(bikes):
            for j, worker in enumerate(workers):
                distances[(abs(bike[0] - worker[0]) + abs(bike[1] - worker[1]))].append((i, j))
        
        for key in sorted(distances.keys()):
            for i in range(len(distances[key])):
                if res[distances[key][i][1]] == -1 and distances[key][i][0] not in taken_bikes:
                    res[distances[key][i][1]] = distances[key][i][0]
                    taken_bikes.add(distances[key][i][0])
                
        return res