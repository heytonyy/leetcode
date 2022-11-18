// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var repeatedNTimes = function(nums) {
    const dict = {}
    const n = nums.length/2
    for (const num of nums){
        (num in dict) ? dict[num]++ : dict[num]=1
    }
    for (const [key,val] of Object.entries(dict)){
        if (val === n){
            return key
        }
    }
    return null
};