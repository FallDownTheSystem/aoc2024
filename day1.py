"""
Advent of Code 2024 - Day 1
"""

from collections import Counter
from aoc_helper import get_input, parse_input


def part1(data: list[str]) -> int:
    """Solve part 1."""
    # Get the numbers on the left and right into seperate lists,
    # sort them, and then sum the differences.
    left, right = seperate_lists(data)

    left.sort()
    right.sort()
    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    return total


def seperate_lists(data):
    left = []
    right = []
    for line in data:
        numbers = line.split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))
    return left, right


def test_part1():
    test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
    data = parse_input(test_input)
    assert part1(data) == 11


def part2(data: list[str]) -> int:
    """Solve part 2."""
    # Get the number of instances of each number on the right list
    left, right = seperate_lists(data)
    right = Counter(right)

    # for each number on the left, find the number of times it appears on the right list
    total = 0
    for number in left:
        total += number * right[number]

    return total


def test_part2():
    test_input = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
    data = parse_input(test_input)
    assert part2(data) == 31


if __name__ == "__main__":
    puzzle_input = get_input(1)
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
