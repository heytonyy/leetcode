// https://leetcode.com/problems/group-anagrams/submissions/

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
 var groupAnagrams = function(strs) {
    const dict = {}
    const result = []
    for (let word of strs){
        const anagram = word.split('').sort().join('');
        (anagram in dict) ? dict[anagram].push(word) : dict[anagram]=[word];
    }
    for (const key of Object.keys(dict)){
        result.push(dict[key])
    }
    return result
};