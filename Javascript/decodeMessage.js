// https://leetcode.com/problems/decode-the-message/

/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */
 var decodeMessage = function(key, message) {
    const letters = [...Array(26)].map((val, i) => String.fromCharCode(i + 97));
    const cypherDict = {}
    const noSpaces = key.replace(/ /g, '')
    let result = ''
    for (let i=0; i<noSpaces.length; i++) {
        if (!(noSpaces[i] in cypherDict)) {
            cypherDict[noSpaces[i]]=letters[0]
            letters.splice(0,1)
        } 
    }
    for (const letter of message){
        result += (letter !== ' ') ? cypherDict[letter] : ' '
    }
    return result
};