package main

import "fmt"

func main() {
	var x int
	fmt.Print("> ")
	n, msg := fmt.Scanln(&x)
	fmt.Println(n, x)
	fmt.Println(msg) // Error message
}
