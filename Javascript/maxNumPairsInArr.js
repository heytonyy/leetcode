// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var numberOfPairs = function(nums) {
    const numDict = {}
    let pairs = 0
    for (const num of nums){
        if (num in numDict) {
            pairs++
            delete numDict[num]
        } else {
            numDict[num]=1
        } 
    }
    return [pairs, Object.keys(numDict).length]
};