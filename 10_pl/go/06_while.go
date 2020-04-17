package main

import "fmt"

func main() {
    s := 1
    // Only Condition
    for s <= 60 {
        s += s
    }
    fmt.Println(s)
}

