def solution(matrix):
    res = []
    # iterate through row & column until we find a non-zero element
    # once we found it, then calculate the square size & go through the boundary#
    # O(squaresize^2) (check if the index is in the boundary)
    # if we find an elem greater than the middle, then break and continue the search 
    # else add the index to the result array
    row = len(matrix)
    col = len(matrix[0])

    for r in range(row):
        for c in range(col):
            current = matrix[r][c]
            searchSize = current*2 +1
            # if abs(x[0]) == abs(x[1] ) continue
            pos = []
            search = searchSize//2
            for x in range(-search,search+1):
                for y in range(-search,search+1):
                    pos.append((x,y))
            flag = False
            
            # if current isn't equal to 0 then break
            if current != 0:
                for p in pos:
                    tempRow = r+p[0]
                    tempCol = c+p[1]
    
                    if (tempRow >= 0 and tempRow < row and tempCol >= 0 and tempCol < col and (abs(p[0]) - abs(p[1]) != 0)):
                        # print(tempRow,",",tempCol)
                        if matrix[tempRow][tempCol] > current:
                            flag = True
                            break
                if not flag:
                    res.append([r,c])
    return res

matrix = [[9,0,0,0,0],
          [0,0,1,0,0],
          [0,0,2,0,0],
          [0,0,0,0,0],
          [0,0,9,0,0],
          [0,3,0,0,3]]

print(solution(matrix))