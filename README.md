# aoc-python

This repository contains my solutions to the Advent of Code event, written in Python.

## Structure:
- The repository is organized by year, with the current year (2024) as the starting folder.
- Each year folder contains subfolders for each day of the event, with the following structure:
  - An executable Python script for the solution.
  - An input file for the day's challenge.

## Future Additions:
- The structure is flexible, allowing for the addition of solutions from other years if desired.

## Astral Dev Tools:
Some handy [uv](https://docs.astral.sh/uv/) & [ruff](https://docs.astral.sh/ruff/) commands I used along the way.
- `uv run src/2024/Day01/day01.py` to run the file.
- `uv tool run ruff format src/2024/Day01/day01.py` to format the file
- `uv tool run ruff check src/2024/Day01/day01.py` to check the file