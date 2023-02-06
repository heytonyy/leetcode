// https://leetcode.com/problems/zigzag-conversion/

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows === 1) {
        return s;
    }

    const zigZagMap = {};
    for (let i=1; i<=numRows; i++) {
        zigZagMap[i]=[];
    }

    let counter = 1
    let increment = true
    for (let letter of s) {
        zigZagMap[counter].push(letter);
        if (counter === 1) increment = true;
        if (counter === numRows) increment = false;
        increment ? counter++ : counter--;
    }

    let output = ''
    for (let row of Object.keys(zigZagMap)){
        for (let letter of zigZagMap[row]) {
            output += letter
        }
    }

    return output
};