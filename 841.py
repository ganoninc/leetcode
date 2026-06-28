from typing import List


class Solution:
    def dfs(self, rooms : List[List[int]], room : int , visited_rooms: set[int]):
        if room not in visited_rooms:
            visited_rooms.add(room)

            for key in rooms[room]:
                self.dfs(rooms, key, visited_rooms)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set()
        self.dfs(rooms, 0, visited_rooms)
        
        return len(visited_rooms) == len(rooms)

        