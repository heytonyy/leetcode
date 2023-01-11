/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    //base cases
    if (p === null && q === null) {
        return true
    }
    if (p === null || q === null) {
        return false
    }
    //recursive cases
    return p.val===q.val && isSameTree(p.left,q.left) && isSameTree(p.right,q.right)
};