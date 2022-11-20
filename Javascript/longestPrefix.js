// https://leetcode.com/problems/longest-common-prefix/submissions/

/**
 * @param {string[]} strs
 * @return {string}
 */
 var longestCommonPrefix = function(strs) {
    min = strs[0].length
    prefix = ''
    for (const word of strs){
        (word.length < min) ? min=word.length : null
    }
    for (let i=0; i<min; i++){
        if (strs.every(word => word[i] === strs[0][i])){
            prefix += strs[0][i]
        } else {
            break
        }
    }
    return prefix
};