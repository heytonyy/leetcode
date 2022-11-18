// https://leetcode.com/problems/two-sum/submissions/


/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    let dict = {}

    for (let i=0; i<nums.length; i++){
        // check if pair is in dictionary
        if (nums[i] in dict){
            return [dict[nums[i]], i]
        }
        
        // add pair to dictionary
        dict[target - nums[i]] = i
    }

    return -1
};