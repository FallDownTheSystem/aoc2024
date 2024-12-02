"""
Advent of Code 2024 - Day 2
"""

from aoc_helper import get_input, parse_input


def part1(data: list[str]) -> int:
    """Solve part 1."""
    safe_lines = 0

    for line in data:
        numbers = [int(n) for n in line.split()]
        safe = True
        increasing = numbers[1] > numbers[0]

        for i in range(len(numbers) - 1):
            diff = numbers[i + 1] - numbers[i]
            if not (1 <= abs(diff) <= 3 and (diff > 0) == increasing):
                safe = False
                break

        if safe:
            safe_lines += 1

    return safe_lines


def test_part1():
    test_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    data = parse_input(test_input)
    assert part1(data) == 2


def is_safe(nums):
    if len(nums) < 2:
        return True
    increasing = nums[1] > nums[0]
    return all(1 <= abs(b - a) <= 3 and (b > a) == increasing for a, b in zip(nums, nums[1:]))


def part2(data: list[str]) -> int:
    safe_count = 0
    for line in data:
        nums = [int(n) for n in line.split()]
        if is_safe(nums) or any(is_safe(nums[:i] + nums[i + 1 :]) for i in range(len(nums))):
            safe_count += 1
    return safe_count


def test_part2():
    test_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
    data = parse_input(test_input)
    assert part2(data) == 4


if __name__ == "__main__":
    puzzle_input = get_input(2)
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
