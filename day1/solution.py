import argparse
from pathlib import Path


def move_dial(dial, direction, points):
    if direction == "L":
        dial = (dial - points) % 100
    elif direction == "R":
        dial = (dial + points) % 100
    return dial


parser = argparse.ArgumentParser()
parser.add_argument("file_path", help="Input File Path")
args = parser.parse_args()

if not Path(args.file_path).exists():
    print("Error: Invalid File Path")
    exit()

challenge_input = []
with open(args.file_path) as f:
    challenge_input = f.readlines()

zero_count = 0
dial = 50  # default value
for line in challenge_input:
    line = line.strip("\n")
    num = int(line[1:])
    direction = line[0]
    dial = move_dial(dial, direction, num)
    if dial == 0:
        zero_count += 1
    print(f"The dial is rotated {line} to point at {dial}")

print(f"Zero count is: {zero_count}")
