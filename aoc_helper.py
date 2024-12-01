"""
Helper functions for Advent of Code 2024.
"""

from pathlib import Path
import requests
import os


def fetch_input(day: int) -> str | None:
    """
    Fetch input for given day from Advent of Code website.
    Uses session cookie from AOC_SESSION_COOKIE environment variable.
    """
    session_cookie = os.environ.get("AOC_SESSION_COOKIE")
    if not session_cookie:
        print("Error: AOC_SESSION_COOKIE environment variable not set")
        return None

    url = f"https://adventofcode.com/2024/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching input: {e}")
        return None


def save_input(day: int, input_data: str) -> bool:
    """Save input data to inputs directory."""
    input_dir = Path(__file__).parent / "inputs"
    input_dir.mkdir(exist_ok=True)

    input_path = input_dir / f"day{day}.txt"
    try:
        input_path.write_text(input_data)
        return True
    except Exception as e:
        print(f"Error saving input: {e}")
        return False


def parse_input(input_data: str) -> list[str]:
    """Parse input data into a newline separated list of trimmed strings."""
    return [line.strip() for line in input_data.strip().split("\n")]


def get_input(day: int) -> list[str] | None:
    """
    Get input for given day. If input file doesn't exist,
    fetch it from the website and save it.
    """
    input_path = Path(__file__).parent / "inputs" / f"day{day}.txt"

    if input_path.exists():
        input_data = input_path.read_text()
    else:
        input_data = fetch_input(day)
        save_input(day, input_data)
    if input_data:
        return parse_input(input_data)
    return None
