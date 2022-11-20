// https://leetcode.com/problems/longest-palindromic-substring/

const s1 = 'babad'
const exp1 = 'bab'

const s2 = "cbbd"
const exp2 = "bb"

const s3 = "ccc"
const exp3 = "ccc"

/**
 * @param {string} s
 * @return {string}
 */
 var longestPalindrome = function(s) {
    let longest = s[0]
    if (s.length === 1){
        return longest
    }
    if (s.length === 2 && s[0]!==s[1]){
        return longest
    }
    for (let i=0; i<s.length; i++){
        for (let j=i+1; j<s.length; j++){
            const substr = s.substring(i,j+1)
            const mid = Math.floor(substr.length/2)
            let pointerI = 0
            let pointerJ = substr.length-1
            let count = 0
            while (pointerI < pointerJ){
                if (substr[pointerI]===substr[pointerJ]){
                    count++
                    pointerI++
                    pointerJ--
                } else {
                    break
                }
            }
            if (count === mid && substr.length > longest.length){
                longest=substr
            }
        }
    }
    return longest
};


console.log(longestPalindrome(s3))