from collections import defaultdict
from collections import deque

# Import nickname list
nicknames = {}
with open("nicknames.txt", 'r') as f:
    for line in f:
        number, name = line.split()
        nicknames[name] = int(number)


# Import link list
links = defaultdict(list)
with open("links.txt", 'r') as f:
    for line in f:
        x, y = map(int,line.split())
        links[x].append(y)


# Breadth first search
def search_target(start, goal):
    queue = deque([start])
    checked = {start}
    count = 0
    while(len(queue)>0):
        if goal in checked:
            return count
        print(queue[0], links[queue[0]])
        queue += list(set(links[queue[0]]) - checked)
        queue.popleft()
        count += 1
    return ("Not found")


# Read names 
start_name, goal_name = input().split()
start = nicknames[start_name]
goal = nicknames[goal_name]
print(start_name, start, goal_name, goal)
print(search_target(start, goal))
    





