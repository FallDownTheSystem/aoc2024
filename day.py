"""
Advent of Code 2024 - Day x
"""

from aoc_helper import get_input, parse_input


def part1(data: list[str]) -> int:
    """Solve part 1."""
    return 0


def test_part1():
    test_input = """
sample
input
here
"""
    data = parse_input(test_input)
    assert part1(data) == 0


def part2(data: list[str]) -> int:
    """Solve part 2."""
    return 0


def test_part2():
    test_input = """
sample
input
here
"""
    data = parse_input(test_input)
    assert part2(data) == 0


if __name__ == "__main__":
    puzzle_input = get_input(x)
    print(f"Part 1: {part1(puzzle_input)}")
    print(f"Part 2: {part2(puzzle_input)}")
