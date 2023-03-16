''.join

def tab_grid_traveler(row, col):
    # trivial cases
    if row == 0 or col == 0:
        return 0
    # generate table ( list comp with for..in loops, dont use [[0]*n]*m] )
    table = [ [ 0 for _ in range(col+1) ] for _ in range(row+1) ]
    # update given values (1 path for a 1x1)
    table[1][1] = 1

    for i in range(1, row+1):
        for j in range(1, col+1):
            # reached the bottom right, return value
            if row == i and col == j:
                return table[row][col]
            # end of row: prevent i out of range
            if row == i and col != j:
                table[i][j+1] += table[i][j]
            # end of col: prevent j out of range
            elif col == j and row != i:
                table[i+1][j] += table[i][j]
            # update regularly
            else:
                table[i][j+1] += table[i][j]
                table[i+1][j] += table[i][j]

test_cases = [
    [(0,0), 0],
    [(0,1), 0],
    [(1,1), 1],
    [(3,3), 6],
    [(2,4), 4],
    [(5,5), 70],
    [(25,25), 32247603683100],
]

# TESTING
for t in test_cases:
    row, col = t[0]
    expected = t[1]
    result = 'PASSED!' if tab_grid_traveler(row,col) == expected else 'FAILED!'
    print(f'Testing {row}x{col} grid -- Expected: {expected} -- Result: {result}')
