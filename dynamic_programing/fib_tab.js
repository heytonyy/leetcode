const fibTab = (n) => {
    const table = Array(n + 1).fill(0)
    table[1] = 1
    for (let i = 0; i <= n; i++){
        table[i+1] += table[i]
        table[i+2] += table[i]
        // console.log(table[i+2])
    }
    return table[n]
}

// TESTING
// console.log(fibTab(0)) // 0
// console.log(fibTab(4)) // 3
// console.log(fibTab(6)) // 8
// console.log(fibTab(9)) // 34
console.log(fibTab(100)) // 354224848179261915075