// https://leetcode.com/problems/length-of-last-word/submissions/

/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLastWord = function(s) {
    const words = s.trim()
    let stack = ''
    for (let i=0; i<words.length; i++){
        letter = words[i]
        if (i === words.length-1){
            return stack.length + 1 // why do i have to +1?s
        }
        if (letter === ' ' && stack.length === 0){
            continue
        }
        if (letter === ' '){
            stack = ''
            continue
        }
        stack+=letter
    }
};