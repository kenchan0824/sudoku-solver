from backtrack import getBlock, checkComplete

def makeCSP(X):

    D = {}  # domain for each variable
    for row in range(0, 9):
        for col in range(0, 9):
            if X[row][col] != 0: continue

            d = [v for v in range(1, 10)]
            d = [v for v in d if v not in X[row]]
            for i in range(0, 9):
                d = [v for v in d if v != X[i][col]]
            
            block = getBlock(X, row, col)
            for block_row in block:
                d = [v for v in d if v not in block_row]
            
            D[(row, col)] = d
                
    return D


def solve(X, D):

    # return true if complete
    if checkComplete(X): return True
    
    # backtrack if no remaining values
    if not D: return False
        
    # choose variable to assign
    mrv = None  # variable with minimum remaining values
    best = 9
    for row, col in D:
        n = len(D[(row, col)])
        if n < best:
            best = n
            mrv = row, col
            if best == 1: break
    
    # choose value
    row, col = mrv
    for value in D[mrv]:
        
        # update X, CSP
        D_ = {}        
        for i, j in D:
            if (i, j) == mrv: continue
            D_[(i, j)] = D[(i, j)].copy()
            
            cond1 = (i == row)
            cond2 = (j == col)
            
            block_row = int(row / 3) * 3
            block_col = int(col / 3) * 3
            cond3 = i in range(block_row, block_row + 3) and \
                    j in range(block_col, block_col + 3)
            
            if (cond1 or cond2 or cond3):
                try:
                    D_[(i, j)].remove(value)
                    if not D_[(i, j)]: del D_[(i, j)]
                except:
                    pass
        
        X[row][col] = value
        # recursive call to subproblem
        if solve(X, D_): return True
        del D_
        
    # revert X, CSP and backtrack
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
    CSP = makeCSP(X)
    solve(X, CSP)
    end = time.time()
    
    print(X)
    print('elapsed %.4f seconds.' % (end - start))

