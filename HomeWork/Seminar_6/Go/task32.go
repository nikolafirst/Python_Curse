// # Задача 32:
// # Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
// # (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

// # На входе : [ 1, 5, 88, 100, 2, -4]
// # 33
// # 200
// # Ответ: [2, 3]

package main

import (
	"fmt"
)

func findIndexInRange(array []int, min, max int) []int {
	var index []int
	for i, num := range array {
		if num >= min && num <= max {
			index = append(index, i)
		}
	}
	return index
}

func main() {
	array := []int{1, 5, 88, 100, 2, -4}
	min := 33
	max := 200

	indexes := findIndexInRange(array, min, max)

	fmt.Println("Ответ:", indexes)
}
