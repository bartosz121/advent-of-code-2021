# not proud of this one; its late im half asleep i will refactor it tomorrow x)
from typing import NamedTuple
from itertools import chain


class Shape(NamedTuple):
    x: int
    y: int


grid = [[int(n) for n in line.strip()] for line in open("input.txt", "r")]
shape = Shape(len(grid[0]), len(grid))


def flash(pos, flashed) -> int:
    """
    pos[0] = y
    pos[1] = x
    """
    y, x = pos
    flashed.append((y, x))
    adj_flashed = 0
    grid[y][x] = 0

    # (y, x)
    adjacent_pos = (
        (-1, 0),  # N
        (-1, 1),  # NE
        (0, 1),  # E
        (1, 1),  # SE
        (1, 0),  # S
        (1, -1),  # SW
        (0, -1),  # W
        (-1, -1),  # NW
    )
    for a_pos in adjacent_pos:
        dy = y + a_pos[0]
        dx = x + a_pos[1]
        if 0 <= dy < shape.y and 0 <= dx < shape.x:
            if (dy, dx) in flashed:
                continue
            grid[dy][dx] += 1
            if grid[dy][dx] > 9:
                flashed.append((dy, dx))
                grid[dy][dx] = 0
                adj_flashed += 1
                adj_flashed += flash((dy, dx), flashed)
    return adj_flashed


def main():
    # n_steps = 100  # uncomment for part 1

    # part 2
    n_steps = 999  # change this to bigger number if you dont get the answer for part 2
    part1_score = 0

    for step in range(n_steps):
        flashed = []
        # part 2
        if sum(chain(*grid)) == 0:
            print(f"part 2: {step}")
            break
        for y in range(shape.y):
            for x in range(shape.x):
                if (y, x) in flashed:
                    continue
                grid[y][x] += 1
                if grid[y][x] > 9:
                    part1_score += 1
                    part1_score += flash((y, x), flashed)
    print(f"{part1_score=}")


if __name__ == "__main__":
    main()
