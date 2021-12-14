from functools import reduce
from operator import mul
from typing import NamedTuple


class Shape(NamedTuple):
    x: int
    y: int


input = [tuple(int(n) for n in line.strip()) for line in open("input.txt", "r")]


def find_basin_size(start_point, shape, seen=None) -> int:
    if seen is None:
        seen = []

    result = 0
    y, x = start_point
    n = input[y][x]

    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    for d in directions:
        dy = y + d[0]
        dx = x + d[1]

        if (dy, dx) in seen:
            continue

        if 0 <= dy < shape.y and 0 <= dx < shape.x:
            n2 = input[dy][dx]

            if n2 == 9:
                continue

            if n2 > n:
                seen.append((dy, dx))
                result += find_basin_size((dy, dx), shape, seen) + 1

    return result


def main():
    part_1 = 0

    low_points: list[tuple(int, int)] = []

    shape = Shape(len(input[0]), len(input))
    # print(shape)

    # N, E, S, W
    directions = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    )

    for y in range(shape.y):
        for x in range(shape.x):
            is_low_point = True
            n = input[y][x]

            if n == 9:
                continue

            for d in directions:
                dy = y + d[0]
                dx = x + d[1]

                if 0 <= dy < shape.y and 0 <= dx < shape.x:
                    n2 = input[dy][dx]

                    if n > n2:
                        is_low_point = False

            if is_low_point:
                low_points.append((y, x))
                part_1 += n + 1

    print(f"{part_1=}")

    basins = []

    for lp in low_points:
        basins.append(
            find_basin_size(lp, shape) + 1
        )  # +1 to count the starting low point too

    part_2 = reduce(mul, sorted(basins)[-3:])

    print(f"{part_2=}")


if __name__ == "__main__":
    main()
