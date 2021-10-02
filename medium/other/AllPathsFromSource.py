class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # check for loop and if destination is the only leaf node
        edges_dict = collections.defaultdict(list)
        for edge in edges:
            edges_dict[edge[0]].append(edge[1])
                
        q = collections.deque([(source, set({source}))])
        visited = set()
        
        found = False
        while q:
            src, seen = q.popleft()
            
            # if found leaf node == target return true, false if leaf is not target
            if edges_dict[src] == []:
                if src == destination:
                    found = True
                else:
                    return False

            for next_node in edges_dict[src]:
                # checking for loop
                if next_node in seen:
                    return False
                if next_node not in visited:
                    q.append((next_node, set({*seen, next_node})))
                    visited.add(next_node)
        
        return found