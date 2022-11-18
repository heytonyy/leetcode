// https://leetcode.com/problems/rings-and-rods/

/**
 * @param {string} rings
 * @return {number}
 */
 var countPoints = function(rings) {
    const ringDict = {}
    let count = 0
    for (let i=0; i<rings.length; i+=2){
        if (rings[i+1] in ringDict){
            ringDict[rings[i+1]].push(rings[i]) 
        } else {
            ringDict[rings[i+1]] = [rings[i]]
        }
    }
    for (const key of Object.keys(ringDict)){
        ['B','G','R'].every(el => ringDict[key].includes(el)) ? count++ : null
    }
    return count
};

