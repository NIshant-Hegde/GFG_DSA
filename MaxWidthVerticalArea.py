def maxWidthOfVerticalArea(points):
    x_cord = []

    for cord in points:
        x_cord.append(cord[0])

    x_cord.sort()

    max_width = x_cord[1] - x_cord[0]

    for i in range(2, len(x_cord)):
        if (x_cord[i] - x_cord[i - 1]) >= max_width:
            max_width = x_cord[i] - x_cord[i - 1]
    
    return max_width

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(maxWidthOfVerticalArea(points))