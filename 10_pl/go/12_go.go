package main

import (
    "fmt"
    "runtime"
    "sync"
)

var wg sync.WaitGroup

func main() {
    runtime.GOMAXPROCS(12)

    // Make channel
    c := make(chan int, 100)

    // Send channel
    for i:=0; i<100; i++ {
        wg.Add(1)
        go func() {
            s := sum(1000000)
            c <- s
        }()
    }
    wg.Wait()
    close(c)

    // Receive channel
    s := 0
    for j := range c {
        s += j
    }
    fmt.Println(s)
}

func sum(n int) int {
    s := 0
    for i:=1; i<=n; i++ {
        s += i
    }
    return s
}
