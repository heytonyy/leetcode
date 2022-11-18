// https://leetcode.com/problems/count-the-number-of-consistent-strings/


/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    let count = 0
    for (const word of words){
        let isValid = true
        for (const letter of word){
            if (!allowed.includes(letter)){
                isValid = false
            }
        }
        isValid ? count++ : null
    }
    return count
};