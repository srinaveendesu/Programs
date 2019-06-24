"""
Problem : Given a set of nodes and its edge links
find the max length that can be reached/traversed

Input format : no. of nodes, no. of links
                Followed by all the links

Example:

5 6
1 2
2 3
3 1
4 2
3 4
3 5

solution: 4

taking node 1 =>  1-> 2 -> 3 -> 4

"""

from collections import defaultdict
a = list(map(int,input().split(' ')))
lst = []
for _ in range(0,a[-1]):
    lst.append(input().split(' '))

def DFS(G,v,seen=None,path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
        if t not in seen:
            t_path = path + [t]
            paths.append(tuple(t_path))
            paths.extend(DFS(G, t, seen[:], t_path))
    return paths
temp_list = []
G = defaultdict(list)
for (s,t) in lst:
    G[s].append(t)
    temp_list.append(s)
    #G[t].append(s)

temp_list = set(temp_list)
# Run DFS, compute metrics
all_paths = []
for val in temp_list:
    all_paths.append(DFS(G, val))

all_len = []
for paths in all_paths:
    for val in paths:
        all_len.append(len(val))
#print (all_len)
max_lenn = max(all_len)
max_paths = [j for p in all_paths for j in p if len(j) == max_lenn]



print("All Paths:")
print(all_paths)
print("Longest Paths:")
for p in max_paths: print("  ", p)
print("Longest Path Length:")
print(max_lenn)
