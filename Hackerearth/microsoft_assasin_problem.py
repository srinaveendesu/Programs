m = 0
n = 0
mat = []
vis = []
#new_mat = []


def dfs(x,y):
    if (x < 0 or x >= m or y < 0 or y >= n or vis[x][y] or mat[x][y]):
        return False

    vis[x][y] = 1

    if (x == m - 1) and (y == n - 1):
        return True

    return dfs(x - 1, y) or dfs(x + 1, y) or dfs(x, y - 1) or dfs(x, y + 1)

def solution(B):
    # write your code in Python 3.8.10

    for i in range(0, len(B)):
        B[i] = list(B[i])

    global m
    global n
    global mat
    global vis
    m = len(B)
    n = len(B[0])
    for _ in range(m):
        tmp = []
        for _ in range(n):
            tmp.append(0)
        mat.append(tmp)
    for _ in range(m):
        tmp = []
        for _ in range(n):
            tmp.append(0)
        vis.append(tmp)

    #print(mat)
    x = 0
    y = 0
    for i in range(m):
        for j in range(n):
            if (B[i][j] == 'X'):
                mat[i][j] = 1

            elif (B[i][j] == '>'):
                mat[i][j] = 1
                for k in range(j+1, n):
                    if (B[i][k] == 'A'):
                        return False
                    if (B[i][k] != '.'):
                        break
                    mat[i][k] = 1

            elif (B[i][j] == '^'):
                mat[i][j] = 1
                for k in range(i, -1, -1):
                    if (B[k][j] == 'A'):
                        return False
                    if (B[k][j] != '.'):
                        break
                    mat[k][j] = 1

            elif (B[i][j] == '<'):
                mat[i][j] = 1
                for k in range(j-1, -1, -1):
                    if (B[i][k] == 'A'):
                        return False
                    if (B[i][k] != '.'):
                        break
                    mat[i][k] = 1
            elif (B[i][j] == '.'):
                continue
            elif (B[i][j] == 'A'):
                x=i
                y=j
                continue
            else:
                mat[i][j] = 1
                for k in range(i+1, m,):
                    if (B[k][j] == 'A'):
                        return False
                    if (B[k][j] != '.'):
                        break
                    mat[k][j] = 1
    print(B)
    print(mat)
    return dfs(x, y)
mat = []
vis = []
print(solution(['X.....>', '..v..X.', '.>..X..', 'A......'])) # flase
mat = []
vis = []
print(solution(['...Xv', 'AX..^', '.XX..'])) #true
mat = []
vis = []
print(solution(['...', '>.A'])) # false
mat = []
vis = []
print(solution(['...', '>.A'])) # false

mat = []
vis = []
print(solution(['X.....<',
                '..v..X.',
                '.>..X..',
                'A......'])) # false

mat = []
vis = []
print(solution(['X.....>',
                '..v..X.',
                '.>.X...',
                'A......'])) # true

mat = []
vis = []
print(solution(['X.....>',
                '..v..X.',
                '.>.X...',
                'A......'])) # true
