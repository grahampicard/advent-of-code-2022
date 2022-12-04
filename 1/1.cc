#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

struct greater {
  template <class T>
  bool operator()(T const &a, T const &b) const {
    return a > b;
  }
};

int getTopCalories(std::string filename) {
  std::string buffer;
  std::ifstream InputFile(filename);
  std::vector<int> calories;
  int elfCalories = 0;
  int topCalories;

  while (getline(InputFile, buffer)) {
    if (buffer == "") {
      calories.push_back(elfCalories);
      if (elfCalories > topCalories) {
        topCalories = elfCalories;
      }
      elfCalories = 0;
    } else {
      elfCalories += std::stoi(buffer);
    }
  }

  calories.push_back(elfCalories);
  if (elfCalories > topCalories) {
    topCalories = elfCalories;
  }

  InputFile.close();
  return topCalories;
}

int getTopThreeCalories(std::string filename) {
  std::string buffer;
  std::ifstream InputFile(filename);
  std::vector<int> calories;
  int elfCalories = 0;

  while (getline(InputFile, buffer)) {
    if (buffer == "") {
      calories.push_back(elfCalories);
      elfCalories = 0;
    } else {
      elfCalories += std::stoi(buffer);
    }
  }

  calories.push_back(elfCalories);
  InputFile.close();

  std::sort(calories.begin(), calories.end(), greater());
  int topThree = 0;
  for (int i = 0; i < 3; i++) {
    topThree += calories[i];
  }

  return topThree;
}

int part1() {
  if (getTopCalories("1_test.txt") != 24000) {
    return 1;
  }
  std::cout << getTopCalories("1_input.txt") << std::endl;
  return 0;
}

int part2() {
  if (getTopThreeCalories("1_test.txt") != 45000) {
    return 1;
  }
  std::cout << getTopThreeCalories("1_input.txt") << std::endl;
  return 0;
}

int main() {
  if (part1() == 1) {
    return 1;
  }
  if (part2() == 1) {
    return 1;
  }
  return 0;
}
