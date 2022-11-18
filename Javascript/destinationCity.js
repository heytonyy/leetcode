// https://leetcode.com/problems/destination-city/

/**
 * @param {string[][]} paths
 * @return {string}
 */
 var destCity = function(paths) {
    const start = paths.map(p => p[0])
    const end = paths.map(p => p[1])
    let current = 0
    while (true) {
        if (start.includes(end[current])) {
            current = start.indexOf(end[current])
        } else {
            return end[current]
        }
    }
};