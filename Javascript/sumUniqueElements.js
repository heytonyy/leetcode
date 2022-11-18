// https://leetcode.com/problems/sum-of-unique-elements/

/**
 * @param {number[]} nums
 * @return {number}
 */
 var sumOfUnique = function(nums) {
    const dict ={}
    let sum = 0
    for (const num of nums){
        if (num in dict){
            dict[num]+=1
        } else {
            dict[num]=1
        }  
    }
    for (const [key,val] of Object.entries(dict)){
        if (val === 1) {
            sum+=parseInt(key)
        }
    }
    return sum
};