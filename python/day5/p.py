from collections import defaultdict

input = [line.strip() for line in open("input.txt", "r")]


def prepare_data(data):
    result = []
    for x in data:
        a, b = x.split(" -> ")

        tuple_a = tuple(map(int, a.split(",")))
        tuple_b = tuple(map(int, b.split(",")))

        result.append((tuple_a, tuple_b))

    return result


def get_points(p1, p2):
    """
    DDA (Digital differential analyzer)
    https://www.youtube.com/watch?v=C8VjggnQRIo
    """
    x1, y1 = p1
    x2, y2 = p2

    # DDA
    dx = x2 - x1
    dy = y2 - y1

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    increment_x = dx // steps
    increment_y = dy // steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        yield (x, y)
        x += increment_x
        y += increment_y


def main():
    data = prepare_data(input)

    grid = defaultdict(int)

    for movement in data:
        start, end = movement
        # Part 1
        # For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2
        # uncomment this if for part 1 solution
        # if not (start[0] == end[0] or start[1] == end[1]):
        #     continue

        for point in get_points(start, end):
            grid[point] += 1

    print(sum(value >= 2 for value in grid.values()))


if __name__ == "__main__":
    main()
