/**
* @param {character[][]} board
* @return {boolean}
 */

const isValidSudoku = (board) => {
    const rowNums = {};
    const colNums = {};
    const boxNums = {};

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            // check to see if it's a number
            if (board[i][j] == '.') {
                continue;
            }
            // ADD NUMBER TO rowNums MAP
            if (rowNums.hasOwnProperty(i)) {
                if (rowNums[i].has(board[i][j])) {
                    return false;
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
                    return false;
                } else {
                    colNums[j].add(board[i][j]);
                }
            } else {
                colNums[j] = new Set();
                colNums[j].add(board[i][j]);
            }

            // FIND OUT WHICH BOX
            let whichBox = '';
            if (i < 3) {
                if (j < 3) {
                    whichBox = '0';
                } else if (j < 6) {
                    whichBox = '1';
                } else {
                    whichBox = '2';
                }
            } else if (i < 6) {
                if (j < 3) {
                    whichBox = '3';
                } else if (j < 6) {
                    whichBox = '4';
                } else {
                    whichBox = '5';
                }
            } else {
                if (j < 3) {
                    whichBox = '6';
                } else if (j < 6) {
                    whichBox = '7';
                } else {
                    whichBox = '8';
                }
            }
            // ADD NUMBER TO boxNums MAP
            if (boxNums.hasOwnProperty(whichBox)) {
                if (boxNums[whichBox].has(board[i][j])) {
                    return false;
                } else {
                    boxNums[whichBox].add(board[i][j]);
                }
            } else {
                boxNums[whichBox] = new Set();
                boxNums[whichBox].add(board[i][j]);
            }
        }
    }
    return true;
};

const testCase = [
    [".", "3", ".", ".", ".", ".", ".", ".", "."], 
    [".", "7", ".", ".", ".", ".", ".", "7", "."], 
    [".", ".", ".", "7", ".", ".", ".", ".", "."], 
    [".", ".", ".", ".", "4", ".", ".", "3", "."], 
    [".", "8", ".", ".", ".", "6", ".", ".", "."], 
    [".", ".", ".", ".", ".", "3", ".", ".", "."], 
    [".", ".", ".", ".", ".", ".", ".", ".", "6"], 
    [".", ".", ".", ".", ".", "8", ".", ".", "."], 
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
]

console.log(isValidSudoku(testCase));