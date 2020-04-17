package main

import "fmt"

func main() {
    s := EvenSum(100)
    fmt.Println(s)
}

func EvenSum(n int) int {
    s := 0
    for i:=1; i<=n; i++ {
        if i % 2 == 0 {
            s += i
        } else {
            continue
        }
    }
    return s
}
