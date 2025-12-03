import argparse
from pathlib import Path


def move_dial_part1(dial, direction, points):
    if direction == "L":
        dial = (dial - points) % 100
    elif direction == "R":
        dial = (dial + points) % 100
    return dial

def move_dial_part2(dial, direction, points):
    zero_count = 0
    for _ in range(points):
        if direction == "L":
            dial = 99 if dial - 1 < 0 else dial - 1
        else:
            dial = 0 if dial + 1 > 99 else dial + 1
        if dial == 0:
            zero_count += 1
    return dial, zero_count


def solve_part1(input: list[str]) -> int:
    zero_count = 0
    dial = 50  # default value
    for line in challenge_input:
        line = line.strip("\n")
        num = int(line[1:])
        direction = line[0]
        dial = move_dial_part1(dial, direction, num)
        if dial == 0:
            zero_count += 1
        print(f"The dial is rotated {line} to point at {dial}")
    return zero_count


def solve_part2(input: list[str]) -> int:
    zero_count = 0
    dial = 50  # default value
    for line in challenge_input:
        line = line.strip("\n")
        num = int(line[1:])
        direction = line[0]
        dial, z_count = move_dial_part2(dial, direction, num)
        zero_count += z_count
        print(f"The dial is rotated {line} to point at {dial} with zero_count of {zero_count}")
    return zero_count


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "part",
        help="The part of the problem to solve (such as 1, 2 or 3 etc)",
        type=int,
    )
    parser.add_argument("file_path", help="Input File Path")
    args = parser.parse_args()

    if not Path(args.file_path).exists():
        raise Exception("Invalid File Path")

    if not args.part:
        raise Exception("Empty or invalid part parameter")

    challenge_input = []
    with open(args.file_path) as f:
        challenge_input = f.readlines()

    zero_count = (
        solve_part1(challenge_input) if args.part == 1 else solve_part2(challenge_input)
    )

    print(f"Zero count: {zero_count}")
