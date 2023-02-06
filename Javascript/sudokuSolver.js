/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
*/

var solveSudoku = function (board) {
    const returnBox = (cell) => {
        const { row, col } = cell;
        if (row < '3') {
            if (col < '3') {
                return '0';
            } else if (col < '6') {
                return '1';
            } else {
                return '2';
            }
        } else if (row < '6') {
            if (col < 3) {
                return '3';
            } else if (col < '6') {
                return '4';
            } else {
                return '5';
            }
        } else {
            if (col < '3') {
                return '6';
            } else if (col < '6') {
                return '7';
            } else {
                return '8';
            }
        }
    };

    const createSudokuMaps = (board) => {
        const rowNums = {};
        const colNums = {};
        const boxNums = {};

        for (let i = 0; i < board.length; i++) {
            for (let j = 0; j < board[0].length; j++) {
                // check to see if it's a number
                if (board[i][j] === '.') {
                    continue;
                }
                // ADD NUMBER TO rowNums MAP
                if (rowNums.hasOwnProperty(i)) {
                    if (rowNums[i].has(board[i][j])) {
                        throw new Error(`Not a valid board`);
                    } else {
                        rowNums[i].add(board[i][j]);
                    }
                } else {
                    rowNums[i] = new Set();
                    rowNums[i].add(board[i][j]);
                }
                // ADD NUMBER TO colNums MAP
                if (colNums.hasOwnProperty(j)) {
                    if (colNums[j].has(board[i][j])) {
                        throw new Error(`Not a valid board`);
                    } else {
                        colNums[j].add(board[i][j]);
                    }
                } else {
                    colNums[j] = new Set();
                    colNums[j].add(board[i][j]);
                }
                // FIND OUT WHICH BOX
                const whichBox = returnBox({ row: i, col: j });

                // ADD NUMBER TO boxNums MAP
                if (boxNums.hasOwnProperty(whichBox)) {
                    if (boxNums[whichBox].has(board[i][j])) {
                        throw new Error(`Not a valid board`);
                    } else {
                        boxNums[whichBox].add(board[i][j]);
                    }
                } else {
                    boxNums[whichBox] = new Set();
                    boxNums[whichBox].add(board[i][j]);
                }
            }
        }
        return { rowNums, colNums, boxNums };
    };

    const nextEmptySpot = (board) => {
        for (let i = 0; i < board.length; i++) {
            for (let j = 0; j < board[0].length; j++) {
                if (board[i][j] === '.') {
                    return { row: i, col: j };
                }
            }
        }
        return null;
    };

    const solveSudokuHelper = (board, rowNums, colNums, boxNums) => {
        // find the first empty spot
        const emptySpot = nextEmptySpot(board);

        // if there is no empty spot, return true
        if (!emptySpot) {
            return true;
        }
        // find out which box it's in
        const whichBox = returnBox(emptySpot);

        // try all possible numbers
        for (let i = 1; i <= 9; i++) {
            console.log(`Checking ${i} @ { Row: ${ emptySpot.row}, Col: ${emptySpot.col}, Box: ${whichBox} }`);
            // check if it's valid option
            if (rowNums[emptySpot.row].has(i.toString()) || colNums[emptySpot.col].has(i.toString()) || boxNums[whichBox].has(i.toString())) {
                continue;
            }
            // if it's valid, add it to the board
            board[emptySpot.row][emptySpot.col] = i.toString();
            rowNums[emptySpot.row].add(i.toString());
            colNums[emptySpot.col].add(i.toString());
            boxNums[whichBox].add(i.toString());
            console.log(`Added ${i} @ { Row: ${ emptySpot.row}, Col: ${emptySpot.col}, Box: ${whichBox} }`);
            // call the helper function again
            if (solveSudokuHelper(board, rowNums, colNums, boxNums)) {
                return true;
            }
            // if it's not valid, remove it from the board
            board[emptySpot.row][emptySpot.col] = '.';
            rowNums[emptySpot.row].delete(i.toString());
            colNums[emptySpot.col].delete(i.toString());
            boxNums[whichBox].delete(i.toString());
            console.log(`Removed ${i} @ { Row: ${ emptySpot.row}, Col: ${emptySpot.col}, Box: ${whichBox} }`);
        }
        return false;
    }

    const { rowNums, colNums, boxNums } = createSudokuMaps(board);
    solveSudokuHelper(board, rowNums, colNums, boxNums);
    console.log(board)
};

const testCase1 = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"],
    [".", ".", ".", "2", "7", "5", "9", ".", "."]
]

const testCase2 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

solveSudoku(testCase2);