package main

import "fmt"

func main() {
    x := 1
    y := 2.0
    z := "hi"
    a := true
    b := false
    i := 3
    fmt.Println(x, y, z, a, b, i)
    fmt.Printf("%T %T %T %T %T %T\n", x, y, z, a, b, i)
}
