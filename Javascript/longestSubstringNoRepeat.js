// https://leetcode.com/problems/longest-substring-without-repeating-characters/

/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLongestSubstring = function(s) {
    let longest = ''
    for (let i=0; i<s.length; i++){
        let substr = s[i]
        for (let j=i+1; j<s.length; j++){
            if (substr.includes(s[j])){
                break
            } else {
                substr+=s[j]
            }
        }
        if (substr.length > longest.length){
            longest=substr
        }
    }
    return longest.length
};