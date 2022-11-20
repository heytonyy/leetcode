// https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/

/**
 * @param {string} s
 * @return {string}
 */
 var reverseWords = function(s) {
    const arr = s.split(' ')
    for (let i=0; i<arr.length; i++){
        arr[i] = arr[i].split('').reverse().join('')
    }
    return arr.join(' ')
};