package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("Hello Japan \n")

	reiwa := time.Date(2019, 4, 1, 0, 0, 0, 0, time.Local)
	now := time.Now()

	fmt.Println("Current time   : ", now)
	fmt.Println("Reiwa Began at : ", reiwa)

	diff := now.Sub(reiwa)
	fmt.Println("Already passed : ", diff)

}
