"""
Given two jugs
You can perform these operations

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

determine if we can get to a state where the combined water of both jugs equal targetCapacity
"""

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        d = gcd(jug1Capacity, jug2Capacity)
                
        return targetCapacity % d == 0 and targetCapacity <= jug1Capacity + jug2Capacity