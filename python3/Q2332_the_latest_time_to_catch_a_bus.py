#
# Difficulty Level: MEDIUM
#
# You are given a 0-indexed integer array buses of length n, where buses[i] represents the departure time of the ith bus.
# You are also given a 0-indexed integer array passengers of length m, where passengers[j] represents the arrival time of the jth passenger.
# All bus departure times are unique.
# All passenger arrival times are unique.
#
# You are given an integer capacity, which represents the maximum number of passengers that can get on each bus.
#
# When a passenger arrives, they will wait in line for the next available bus.
# You can get on a bus that departs at x minutes if you arrive at y minutes where y <= x, and the bus is not full.
# Passengers with the earliest arrival times get on the bus first.
#
# More formally when a bus arrives, either:
#
# • If capacity or fewer passengers are waiting for a bus, they will all get on the bus, or
# • The capacity passengers with the earliest arrival times will get on the bus.
#
# Return the latest time you may arrive at the bus station to catch a bus.
# You cannot arrive at the same time as another passenger.
#
# Note: The arrays buses and passengers are not necessarily sorted.
#

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        index = 0

        for bus in buses:
            cap = capacity
            while cap and index < len(passengers) and passengers[index] <= bus:
                cap -= 1
                index += 1

        latest = bus if cap else passengers[index - 1]

        for curr in range(index - 1, -1, -1):
            if latest == passengers[curr]:
                latest -= 1 
            else:
                break

        return latest