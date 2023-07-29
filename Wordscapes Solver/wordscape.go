package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

// Global Answer Array
var answers []string

func binarySearch(word string, mylist []string) bool {
	// Does a binary search through mylist array
	low := 0
	high := len(mylist) - 1

	for low <= high {
		median := (low + high) / 2

		if mylist[median] < word {
			low = median + 1
		} else {
			high = median - 1
		}
	}

	if low == len(mylist) || mylist[low] != word {
		return false
	}

	return true
}

func join(ins []rune, c rune) (result []string) {
	// appends a string one letter at a time
	for i := 0; i <= len(ins); i++ {
		result = append(result, string(ins[:i])+string(c)+string(ins[i:]))
	}
	return
}

func permutations(testStr string) []string {
	// Finds all permutations of the string inputted
	var n func(testStr []rune, p []string) []string
	n = func(testStr []rune, p []string) []string {
		if len(testStr) == 0 {
			return p
		} else {
			result := []string{}
			for _, e := range p {
				result = append(result, join([]rune(e), testStr[0])...)
			}
			return n(testStr[1:], result)
		}
	}

	output := []rune(testStr)
	return n(output[1:], []string{string(output[0])})
}

func comboUtil(arr []rune, data []string, start int, n int, index int, r int, mylist []string) {
	// Finds every combination of letters and calls permutations() and binarySearch() to find all the answers
	if r == index {
		perm := strings.Join(data, "")
		permArr := permutations(perm)

		for i := 0; i < len(permArr); i++ {
			result := binarySearch(permArr[i], mylist)
			if result == true {
				answers = append(answers, permArr[i])
			}
		}
		return
	}
	for i := start; i < n && n-i+1 >= r-index; i++ {
		data[index] = string(arr[i])
		comboUtil(arr, data, i+1, n, index+1, r, mylist)
	}
}

func printCombo(arr []rune, n int, r int, mylist []string) {
	// Setup for comboUtil()
	data := make([]string, r)
	comboUtil(arr, data, 0, n, 0, r, mylist)
}

func check(e error) {
	// error check
	if e != nil {
		panic(e)
	}
}

func readWords() []string {
	// read each line of words.txt
	i := 0
	f, err := os.Open("wordscapesDictionary.txt")
	check(err)
	defer f.Close()
	var words []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		i++
		words = append(words, scanner.Text())
	}

	check(err)
	return words
}

func deleteDuplicates(arr []string) []string {
	unique := make(map[string]bool)
	result := []string{}

	for _, s := range arr {
		if !unique[s] {
			unique[s] = true
			result = append(result, s)
		}
	}

	return result
}

func main() {
	// call readWords() to read in words return array
	wordsArr := readWords()
	// input
	var input string
	fmt.Println("Enter the letters:")
	fmt.Scanf("%s", &input)
	// make a rune array
	characters := []rune(input)
	// Find all three letter words
	printCombo(characters, len(characters), 3, wordsArr)
	// Find all four letter words
	if len(characters) >= 4 {
		printCombo(characters, len(characters), 4, wordsArr)
	}
	//Find all five letter words
	if len(characters) >= 5 {
		printCombo(characters, len(characters), 5, wordsArr)
	}
	//Find all six letter words
	if len(characters) >= 6 {
		printCombo(characters, len(characters), 6, wordsArr)
	}
	//Find all seven letter words
	if len(characters) >= 7 {
		printCombo(characters, len(characters), 7, wordsArr)
	}
	// Delete duplicate answers
	answers := deleteDuplicates(answers)
	// Print the answers
	fmt.Println("ANSWERS:")
	for i := 1; i < len(answers)+1; i++ {
		fmt.Printf("%d: %s\n", i, answers[i-1])
	}

}
