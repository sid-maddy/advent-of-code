"""Day 1."""

from __future__ import annotations

import string
from pathlib import Path
from typing import Literal

import regex


def calibrate_part1(line: str) -> int:
    """Calibrates the value for the given line.

    The newly-improved calibration document consists of lines of text; each
    line originally contained a specific calibration value that the Elves now
    need to recover. On each line, the calibration value can be found by
    combining the first digit and the last digit (in that order) to form a
    single two-digit number.

    For example:

    1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet

    In this example, the calibration values of these four lines are 12, 38, 15,
    and 77. Adding these together produces 142.
    """
    matches = regex.findall(r"[0-9]", line)
    if not matches:
        return 0

    return int(matches[0] + matches[-1])


Digit = Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
DIGIT_MAP: dict[str, Digit] = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def digit(s: str) -> Digit:
    return DIGIT_MAP.get(s, "0")


def calibrate_part2(line: str) -> int:
    """Calibrates the value for the given line.

    Your calculation isn't quite right. It looks like some of the digits are
    actually spelled out with letters: one, two, three, four, five, six, seven,
    eight, and nine also count as valid "digits".

    Equipped with this new information, you now need to find the real first and
    last digit on each line. For example:

    two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen

    In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
    Adding these together produces 281.
    """
    matches = regex.findall(r"[0-9]|zero|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)
    if not matches:
        return 0

    return int(digit(matches[0]) + digit(matches[-1]))


def main() -> None:
    part1_result = part2_result = 0

    with Path("../input.txt").open() as f:
        for line in f:
            part1_result += calibrate_part1(line)
            part2_result += calibrate_part2(line)

    print(part1_result)
    print(part2_result)


if __name__ == "__main__":
    main()
