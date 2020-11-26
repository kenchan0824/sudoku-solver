def getBlock(X, row, col):

    block_row = int(row / 3) * 3
    rank = X[block_row : block_row + 3]
    block_col = int(col / 3) * 3
    return [rank[i][block_col : block_col + 3] for i in range(0, 3)]


def checkConsistence(X, row, col, value):

    if value in X[row]: return False
    if value in [X[i][col] for i in range(0, 9)]: return False

    block = getBlock(X, row, col)
    if any([value in row for row in block]): return False
    
    return True


def checkComplete(X):
    
    return not any([0 in row for row in X])


def sovle(X):

    if checkComplete(X): return True
    
    for row in range(0, 9):
        for col in range(0, 9):
            if X[row][col] != 0: continue
        
            for value in range(1, 10):
               if checkConsistence(X, row, col, value):
                   X[row][col] = value
                   if sovle(X): return True
            
            # backtrack
            X[row][col] = 0
            return False


if __name__ == '__main__':
    
    import time

    X = []
    X.append([0, 6, 0, 0, 0, 7, 0, 0, 0])
    X.append([1, 0, 0, 0, 8, 0, 0, 0, 4])
    X.append([0, 0, 0, 9, 1, 0, 0, 0, 0])
    X.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    X.append([0, 0, 0, 3, 0, 0, 0, 2, 6])
    X.append([4, 7, 0, 0, 0, 6, 8, 0, 0])
    X.append([6, 0, 5, 0, 0, 2, 4, 7, 0])
    X.append([0, 0, 0, 0, 0, 8, 1, 0, 0])
    X.append([0, 0, 9, 0, 0, 0, 0, 3, 0])

    start = time.time()
    sovle(X)
    print('elapsed %.4f seconds.' % (time.time() - start))
