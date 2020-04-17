package main

import "fmt"

func main() {
    fmt.Println(Add(1, 2))
    fmt.Println(Add_f64(1.0, 2.0))
}

func Add(x, y int) int {
    return x + y
}

func Add_f64(x, y float64) float64 {
    return x + y
}
