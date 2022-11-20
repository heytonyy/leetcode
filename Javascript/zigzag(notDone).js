/*
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
*/

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
 var convert = function(s, numRows) {
    const subArrs = []
    let output = ''
    const groups = Math.ceil(s.length/(numRows+1))
    for (let i=0; i<s.length; i+=groups){
        subArrs.push(s.slice(i,i+numRows+1).split(''))
    }
    for (let j=0; j<subArrs.length; j++){
        output+=subArrs[j][0]
        subArrs[j][0] = subArrs[j].splice(1)
    }
    return output, subArrs
};


// // // /// /// // /// /// / // // // / /
const s1 = "PAYPALISHIRING"
const numRows1 = 3
const exp1 = "PAHNAPLSIIGYIR"
/*
P   A   H   N
A P L S I I G
Y   I   R
*/

const s2 = "PAYPALISHIRING"
const numRows2 = 4
const exp2 = "PINALSIGYAHRPI"
/*
P     I    N
A   L S  I G
Y A   H R
P     I
*/

console.log(convert(s1, numRows1))
// console.log(convert(s2, numRows2))