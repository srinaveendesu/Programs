### https://fizzbuzzer.com/mud-walls/

'''
A child likes to build mud walls by placing mud between sticks positioned on a number line. The gap between sticks will be referred to as a cell, and each cell will contain one segment of wall. The height of mud in a segment cannot exceed 1 unit above an adjacent stick or mud segment. Given the placement of a number of sticks and their heights, determine the maximum height segment of mud that can be built. If no mud segment can be built, return 0.

For example, there are n = 3 sticks at stickPositions = [1, 2, 4, 7] with stickHeights = [4, 5, 7, 11]. There is no space between the first two sticks, so there is no cell for mud. Between positions 2 and 4, there is one cell. Heights of the surrounding sticks are 5 and 7, so the maximum height of mud is 5 + 1 = 6. Between positions 4 and 7 there are two cells. The heights of surrounding sticks are 7 and 11. The maximum height mud segment next to the stick of height 7 is 8. The maximum height mud next to a mud segment of height 8 and a stick of height 11 is 9. Mud segment heights are 6, 8 and 9, and the maximum height is 9. In the table below, digits are in the columns of sticks and M is in the mud segments.
'''


def maxHeight(wallPositions, wallHeights):
    # Write your code here
    max_h = 0
    n = len(wallPositions)
    m = len(wallHeights)
    max_h = 0
    localmax = 0
    for i in range(0,n-1):

        if wallPositions[i]< wallPositions[i+1]-1:
            h_diff = abs(wallHeights[i] -wallHeights[i+1])
            gap = wallPositions[i+1] -wallPositions[i] -1
            l = 0

            if gap>h_diff:
                a,b = wallHeights[i],wallHeights[i+1]
                low = max(a,b) +1
                r_gap = gap - h_diff -1
                localmax = low + r_gap/2
            else:
                localmax = min(wallHeights[i],wallHeights[i+1]) +gap
        print(localmax,max_h)
        max_h = max(localmax,max_h)

    print(max_h)
    return max_h



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    wallPositions_count = int(input().strip())

    wallPositions = []

    for _ in range(wallPositions_count):
        wallPositions_item = int(input().strip())
        wallPositions.append(wallPositions_item)

    wallHeights_count = int(input().strip())

    wallHeights = []

    for _ in range(wallHeights_count):
        wallHeights_item = int(input().strip())
        wallHeights.append(wallHeights_item)

    result = maxHeight(wallPositions, wallHeights)

'''
3
1
3
7
3
4
3
3


1 3 7
4 3 3
output :

5

sample input : 
4
1
2
4
7
4
4
5
7
11 

sample output : 9
'''