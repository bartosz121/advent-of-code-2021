from collections import defaultdict


def main():
    """
    There is no need to count every fish individually;
    Count 'types' [0-8] in dictionary instead;
    Clear 'fishes_2' dict have to be created and then assigned to 'fishes' to avoid summing up fishes between days
    """
    with open("input.txt", "r") as f:
        data = [int(n) for n in f.readline().split(",")]

    fishes = defaultdict(int)

    for initial in data:
        fishes[initial] += 1

    # part 1
    # for day in range(80):
    for day in range(256):
        fishes_2 = defaultdict(int)
        for fish_type, count in fishes.items():
            if fish_type == 0:
                fishes_2[6] += count
                fishes_2[8] += count
            else:
                fishes_2[fish_type - 1] += count

        fishes = fishes_2

        print(f"DAY {day}: {sum(fishes.values())}")


if __name__ == "__main__":
    main()
