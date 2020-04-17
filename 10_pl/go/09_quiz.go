package main

import (
    "fmt"
)

func main() {
    a1, _ := seq(6)
    fmt.Println(a1)
    _, s := seq(100)
    fmt.Println(s)
}

func seq(n int) (int, int) {
    a := 91
    s := 0
    for i:=1; i<n; i++ {
        if i%2 == 0 {
            a = a / 2
        } else {
            a += 1
        }
        s += a
        if a == 1 {
            fmt.Println(i)
            return a, s
        }
    }
    return a, s
}
