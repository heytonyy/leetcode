// https://leetcode.com/problems/flipping-an-image/

/**
 * @param {number[][]} image
 * @return {number[][]}
 */
 var flipAndInvertImage = function(image) {
    for (let i=0; i<image.length; i++) {
        // midpoint
        let mid = Math.floor(image[i].length/2)
        // if odd --> swap mid
        if (image[i].length % 2 === 1) {
            if (image[i][mid] === 0){
                image[i][mid] = 1
            } else {
                image[i][mid] = 0
            }
        }
        // swap and changes up to mid point
        for (let j=0; j<mid; j++) {
            let oppIdx = image[i].length - 1 - j
            
            let temp = image[i][j]
            image[i][j] = image[i][oppIdx]
            image[i][oppIdx] = temp
             
            if (image[i][j] === 0){
                image[i][j] = 1
            } else {
                image[i][j] = 0
            }

            if (image[i][oppIdx] === 0){
                image[i][oppIdx] = 1
            } else {
                image[i][oppIdx] = 0
            }  
        }
    }
    return image
};