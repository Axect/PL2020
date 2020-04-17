package main

import "fmt"

func main() {
    s := 0
    // Start, Condition, Change
    for i := 0; i <= 10; i++ {
        s += i
    }
    fmt.Println(s)
}
