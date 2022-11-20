/* 
Given two strings,
return true if the first string can be built from the letters in the 2nd string
Ignore case
.indexOf will only tell you if the letter is found one time
*/

const strA1 = "Hello World";
const strB1 = "lloeh wordl";
const expected1 = true;

const strA2 = "Hey";
const strB2 = "hello";
const expected2 = false;
// Explanation: second string is missing a "y"

const strA3 = "hello";
const strB3 = "helo";
const expected3 = false;
// Explanation: second string doesn't have enough "l" letters

const strA4 = "hello";
const strB4 = "lllheo";
const expected4 = true;

const strA5 = "hello";
const strB5 = "heloxyz";
const expected5 = false;
// Explanation: strB5 does not have enough "l" chars.

/**
 * Determines whether s1 can be built using the chars of s2.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean}
 */
function canBuildS1FromS2(s1, s2) {
    const str1 = s1.replace(' ', '').toLowerCase()
    const str2 = s2.replace(' ', '').toLowerCase()
    const dict1 = {}
    if (str1.length > str2.length){
        return false
    }
    for (const letter1 of str1){
        (letter1 in dict1) ? dict1[letter1]++ : dict1[letter1]=1
    }
    let isValid = true
    for (const letter2 of str2) {
        if (letter2 in dict1){
            dict1[letter2]--
        }
    }
    for (const key in dict1){
        if (dict1[key] > 0){
            isValid = false
            break
        }
    }
    return isValid
}

console.log(canBuildS1FromS2(strA3,strB3))

// O(3n) --> O(n)