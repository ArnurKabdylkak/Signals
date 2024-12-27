package main

import (
	"fmt"
	"math"
)

// Решение дифференциального уравнения методом Эйлера
func solveDifferentialEquation(step float64, maxTime float64) []float64 {
	nSteps := int(maxTime / step)
	y := make([]float64, nSteps)
	dy := make([]float64, nSteps)

	for i := 0; i < nSteps-1; i++ {
		t := float64(i) * step
		x := math.Cos(t)
		ddy := x - 3*dy[i] - 2*y[i]

		dy[i+1] = dy[i] + ddy*step
		y[i+1] = y[i] + dy[i]*step
	}

	return y
}

// Разностное уравнение: y[n] - y[n-1] + 0.25y[n-2] = x[n], x[n] = δ[n]
func solveDifferenceEquation(nSteps int) []float64 {
	y := make([]float64, nSteps)
	x := make([]float64, nSteps)
	x[0] = 1 // Дельта-функция

	for n := 2; n < nSteps; n++ {
		y[n] = x[n] + y[n-1] - 0.25*y[n-2]
	}

	return y
}

func main() {
	// Дифференциальное уравнение
	step := 0.01
	maxTime := 10.0
	yDifferential := solveDifferentialEquation(step, maxTime)

	fmt.Println("Решение дифференциального уравнения:")
	for i, y := range yDifferential {
		fmt.Printf("t = %.2f, y = %.4f\n", float64(i)*step, y)
	}

	// Разностное уравнение
	nSteps := 20
	yDifference := solveDifferenceEquation(nSteps)

	fmt.Println("\nРешение разностного уравнения:")
	for n, y := range yDifference {
		fmt.Printf("n = %d, y = %.4f\n", n, y)
	}
}
