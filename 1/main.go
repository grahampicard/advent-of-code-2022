package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
)

func load(input string) []byte {
	content, err := ioutil.ReadFile(input)

	if err != nil {
		log.Fatal(err)
	}

	return content
}

func prepElves(raw []byte) []int {
	data := string(raw)
	unprocessed := strings.Split(data, "\n\n")
	var elves []int
	for _, s := range unprocessed {
		calories := strings.Split(s, "\n")
		var elf int
		for _, calorie := range calories {
			int_cal, err := strconv.Atoi(calorie)
			if err != nil {
				log.Fatal((err))
			}
			elf += int_cal
		}
		elves = append(elves, elf)
	}
	return elves
}

func getMaxElf(input string) int {
	test_data := load(input)
	elves := prepElves(test_data)
	var max_elf int
	for _, elf := range elves {
		if elf > max_elf {
			max_elf = elf
		}
	}
	return max_elf
}

func part1Test() {
	result := getMaxElf("1_test.txt")
	if result != 24000 {
		log.Fatal("uhoh")
	}
}

func part1() {
	result := getMaxElf("1_input.txt")
	fmt.Println(result)
}

func main() {
	part1Test()
	part1()
}
