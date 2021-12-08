from statistics import median
from math import ceil

input = [int(n) for n in open("input.txt", "r").readline().split(",")]

# input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def main():
    # part 1
    m = median(input)
    fuel = int(sum(abs(m - i) for i in input))
    print(fuel)

    # part 2
    max_ = max(input)
    min_ = min(input)

    cheapest = 999_999_999  # maybe more???

    for pos in range(min_, max_ + 1):
        candidate = 0
        for crab_pos in input:
            n = abs(crab_pos - pos)
            candidate += n * (n + 1) // 2

        if candidate < cheapest:
            cheapest = candidate

    print(cheapest)


if __name__ == "__main__":
    main()
