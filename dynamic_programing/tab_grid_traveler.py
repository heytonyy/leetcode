def tab_grid_traveler(row, col):
    # trivial case
    if row == 0 and col == 0:
        return 0
    # generate table ( list comp with for..in loops, dont use [[0]*n]*m] )
    table = [ [ 0 for _ in range(col+1) ] for _ in range(row+1) ]
    # update given values (1 path for a 1x1)
    table[1][1] = 1

    for i in range(1, row+1):
        for j in range(1, col+1):
            # reached the bottom right, return value
            if row - i == 0 and col - j == 0:
                return table[row][col]
            # prevent i out of range
            if row - i == 0 and col - j != 0:
                table[i][j+1] += table[i][j]
            # prevent j out of range
            elif col - j == 0 and row - i != 0:
                table[i+1][j] += table[i][j]
            # update 
            else:
                table[i][j+1] += table[i][j]
                table[i+1][j] += table[i][j]

test_cases = [
    [(0,0), 0],
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
