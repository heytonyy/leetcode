// https://leetcode.com/problems/shuffle-the-array/

/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
 var shuffle = function(nums, n) {
    const left = nums.slice(0,n)
    const right = nums.slice(n,nums.length)
    let arr = []
    for (const i in left){
      arr.push(left[i])
      arr.push(right[i])
    }
    return arr
};