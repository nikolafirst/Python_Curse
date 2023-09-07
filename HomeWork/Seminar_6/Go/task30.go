// # Задача 30:
// # Заполните массив элементами арифметической прогрессии.
// # Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
// # Каждое число вводится с новой строки.

package main

import (
	"fmt"
)

func main() {
	var a1, d, n int
	fmt.Println("Введите первый элемент арифметической прогрессии: ")
	fmt.Scanln(&a1)

	fmt.Println("Введите разность: ")
	fmt.Scanln(&d)

	fmt.Println("Введите количество элементов: ")
	fmt.Scanln(&n)

	progress := make([]int, n)
	for i := 0; i < n; i++ {
		progress[i] = a1 + i*d
	}
	fmt.Println("Массив арифметической прогрессии:", progress)
}
