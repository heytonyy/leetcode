// https://leetcode.com/problems/replace-all-digits-with-characters/submissions/

/**
 * @param {string} s
 * @return {string}
 */
 var replaceDigits = function(s) {
    let output = ''
    const letters = [...Array(26)].map((val, i) => String.fromCharCode(i + 97));
    for (let i=0; i<s.length; i++){
        if (i%2 === 1){
            shift = parseInt(letters.indexOf(s[i-1])) + parseInt(s[i])
            output+=letters[shift]
        } else {
            output+=s[i]
        }
    }
    return output
};