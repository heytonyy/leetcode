// https://leetcode.com/problems/first-letter-to-appear-twice/

/**
 * @param {string} s
 * @return {character}
 */
 var repeatedCharacter = function(s) {
    const dict = {}
    for (const letter of s){
        if (letter in dict){
            return letter
        } else {
            dict[letter]=1
        }
    }
    return null
};