// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
 var kidsWithCandies = function(candies, extraCandies) {
    const maxCandies = Math.max(...candies)
    for (let i=0; i<candies.length; i++){
      (candies[i]+extraCandies>=maxCandies) ? candies[i]=true : candies[i]=false
    }
    return candies
};