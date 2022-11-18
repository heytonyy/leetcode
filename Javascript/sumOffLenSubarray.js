// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

/**
 * @param {number[]} arr
 * @return {number}
 */
 var sumOddLengthSubarrays = function(arr) {
    const odds = []
    for (let i=arr.length; i>0; i-=2) {
      for (let j=0; j<i; j++) {
        odds.push(arr.slice(j,((arr.length-i)+j+1)).reduce((p,a)=>p+a,0))
      }
    }
    return odds.reduce((p,a)=>p+a,0)
};