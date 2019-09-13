### https://fizzbuzzer.com/mud-walls/

def maxHeight(wallPositions, wallHeights):
    # Write your code here
    for i,wp in enumerate(wallPositions):
        print (i,wp)
        if len(wallHeights) > i+1:
            val = abs(wallHeights[i] - wallHeights[i+1])

        print(val)
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

output :

5
'''