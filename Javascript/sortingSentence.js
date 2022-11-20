// https://leetcode.com/problems/sorting-the-sentence/submissions/

/**
 * @param {string} s
 * @return {string}
 */
 var sortSentence = function(s) {
    const dict = {}
    const words = s.split(' ')
    let output = ''
    for (let word of words){
        dict[word.at(-1)] = word.slice(0,word.length-1)
    }
    for (const key in dict){
        output += `${dict[key]} `
    }
    output = output.slice(0,output.length-1)
    return output
};