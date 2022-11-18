// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

/**
 * @param {string} s
 * @return {boolean}
 */
 var areOccurrencesEqual = function(s) {
    const letterDict = {}
    let isGood = true
    for (const letter of s){
        (letter in letterDict) ? letterDict[letter]++ : letterDict[letter]=1
    }
    const freq = Object.values(letterDict)
    for (let i=1; i<freq.length; i++){
        if (freq[i-1]!==freq[i]){
            isGood = false
            break
        }
    }
    return isGood
};