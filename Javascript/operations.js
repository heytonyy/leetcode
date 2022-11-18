// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

/**
 * @param {string[]} operations
 * @return {number}
 */
 var finalValueAfterOperations = function(operations) {
    const ops = {
      '++X': 1,
      'X++': 1,
      '--X': -1,
      'X--': -1
    }
    let total = 0
    for (const o of operations) {
      total += ops[o]  
    }
    return total
};