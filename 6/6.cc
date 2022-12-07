// #include <iostream>
#include <fstream>
#include <iostream>
#include <string.h>
#include <map>
#include <err.h>

int detect_marker(std::string input, int length)
{
    std::string buffer;
    int counter = 0;
    while (input.size() > 0)
    {
        while (buffer.size() < length)
        {
            buffer.push_back(input[0]);
            input.erase(0, 1);
            ++counter;
        }
        std::map<char, int> lookup;
        for (int i = 0; i < buffer.size(); ++i)
        {
            lookup[buffer[i]]++;
        }
        if (lookup.size() == length)
        {
            return counter;
        }
        else
        {
            buffer.erase(0, 1);
        }
    }
    throw std::range_error("Run out of letters");
}

void part_1_tests()
{
    assert(detect_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7);
    assert(detect_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5);
    assert(detect_marker("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6);
    assert(detect_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10);
    assert(detect_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11);
}

void part_2_tests()
{
    assert(detect_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19);
    assert(detect_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23);
    assert(detect_marker("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23);
    assert(detect_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29);
    assert(detect_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26);
}

int main()
{
    // run all tests for part 1 first
    part_1_tests();

    // Run on input file
    std::ifstream file("6_input.txt");
    std::string buffer;
    while (getline(file, buffer))
    {
        int result = detect_marker(buffer, 4);
        std::cout << result << std::endl;
    }

    // run all tests for part 1 first
    part_2_tests();

    // Run on input file
    std::ifstream file2("6_input.txt");
    while (getline(file2, buffer))
    {
        int result = detect_marker(buffer, 14);
        std::cout << result << std::endl;
    }

    return 0;
}