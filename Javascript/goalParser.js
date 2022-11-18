// https://leetcode.com/problems/goal-parser-interpretation/

/**
 * @param {string} command
 * @return {string}
 */
 var interpret = function(command) {
    let output = ''
     for (let i=0; i<command.length; i++){
         if (command[i] == 'G'){
             output += 'G'
         } else if (command[i] == '(' && command[i+1] == 'a') {
             output += 'al'
             i+=3
         } else if (command[i] == '(' && command[i+1] == ')') {
             output += 'o'
             i++
         } else {
             output + command[i]
         }
     }
    return output
};