# Import nickname list
nicknames = {}
with open("nicknames.txt", 'r') as f:
    for line in f:
        number, name = line.split()
        nicknames[name] = int(number)


# Import link list
links = {}
with open("links.txt", 'r') as f:
    for line in f:
        x, y = map(int,line.split())
        if x in links:
            links[x].append(y)
        else:
            links[x] = [y]


# Breadth first search
def search_target(start, goal):
    queue = [start]
    check = [start]
    count = 0
    while(len(queue)>0):
        #print(queue[0], links[queue[0]])
        queue += list(set(links[queue[0]]) - set(check))
        if(goal in check):
            return count
        check += list(set(links[queue[0]]) - set(check))
        queue.pop(0)
        count += 1
    return ("Not found")


# Read names 
start_name, goal_name = input().split()
start = nicknames[start_name]
goal = nicknames[goal_name]
print(start_name, start, goal_name, goal)
print(search_target(start, goal))
    





