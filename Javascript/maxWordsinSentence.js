// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

/**
 * @param {string[]} sentences
 * @return {number}
 */
 var mostWordsFound = function(sentences) {
    const book = {}
    let max = 0
    for (let i=0; i<sentences.length; i++) {
      book[i] = sentences[i].split(' ').length
    }
    for (let j=0; j<sentences.length; j++) {
      if (book[j] > max) {
        max = book[j]
      }
    }
    return max
};