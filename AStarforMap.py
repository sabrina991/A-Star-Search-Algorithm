from collections import defaultdict
from typing import Tuple
from queue import PriorityQueue

def heuristic(start_node: Tuple[int, int], destination_node: Tuple[int, int]) -> int:
    (x1, y1) = start_node
    (x2, y2) = destination_node
    return abs(x1 - x2) + abs(y1 - y2)

class Graph(object):

    def __init__(self, searched_element):
        self.graph = defaultdict(list)
        self.searched_element = searched_element
        self.parent = {}
        self.cost = {}
        self._queue = PriorityQueue()

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def a_star_search(self, start_node):
        self._queue.put(start_node, 0)
        self.parent[start_node] = None
        self.cost[start_node] = 0
        while not self._queue.empty():
            current = self._queue.get()
            if current == self.searched_element:
                break
            for child, weight in self.graph[current]:
                new_cost = self.cost[current] + weight
                if self.bool_next_child(child, new_cost):
                    self.find_next_node(child, current, new_cost)

        # Construct the shortest path
        path = []
        node = self.searched_element
        while node is not None:
            path.insert(0, node)
            node = self.parent[node]

        return path

    def find_next_node(self, child, current, new_cost):
        self.cost[child] = new_cost
        priority = new_cost + heuristic(child, self.searched_element)
        self._queue.put(child, priority)
        self.parent[child] = current

    def bool_next_child(self, child, new_cost):
        return child not in self.cost or new_cost < self.cost[child]


if __name__ == "__main__":
    # Ending node
    g = Graph((11, 8))
    
    #starting_point = (0,0)
    # point a =(2,2)
    # point b =(5,1)
    # point c =(5,5)
    # point d =(3,7)
    # point e =(5,7)
    # point f =(7,4)
    # point g =(7,8)
    # point h =(9,7)
    # point i =(9,5)
    # point j =(10,2)
    # point k =(11,6)
    #ending_point = (11,8)
     
    g.add_edge((0, 0), (2, 2), 4)
    g.add_edge((0, 0), (10, 2), 21)
    g.add_edge((0, 0), (3, 7), 9)
    g.add_edge((2, 2), (5, 1), 6)
    g.add_edge((2, 2), (5, 5), 7)
    g.add_edge((5, 1), (10, 2), 9)
    g.add_edge((5, 1), (9, 5), 8)
    g.add_edge((5, 5), (7, 4), 5)
    g.add_edge((5, 5), (9, 7), 7)
    g.add_edge((5, 5), (7, 8), 6)
    g.add_edge((5, 5), (5, 1), 6)
    g.add_edge((3, 7), (5, 5), 6)
    g.add_edge((3, 7), (5, 7), 3)
    g.add_edge((7, 4), (9, 5), 5)
    g.add_edge((7, 8), (9, 7), 8)
    g.add_edge((7, 8), (11, 8), 8)
    g.add_edge((9, 7), (4, 4), 8)
    g.add_edge((9, 7), (11, 6), 5)
    g.add_edge((9, 7), (11, 8), 4)
    g.add_edge((9, 5), (11, 6), 4)
    g.add_edge((11, 6), (11, 8), 3)
    

    shortest_path = g.a_star_search((0, 0)) # Starting Node
    print("Shortest Path using A* :", shortest_path)