package main

import "fmt"

func main() {
	// 1.
	fmt.Println(A(6))

	// 2.
	n := 1
	for {
		if A(n) == 1 {
			break
		}
		n += 1
	}
	fmt.Println(n)

	// 3.
	m := 1
	s := 0
	for {
		b := A(m)
		if b == 1 {
			s += b
			break
		}
		s += b
		m += 1
	}
	fmt.Println(s)
}

func A(n int) int {
	if n == 1 {
		return 91
	} else if n%2 == 0 {
		return A(n-1) + 1
	} else {
		return A(n-1) / 2
	}
}
