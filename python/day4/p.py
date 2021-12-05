from itertools import chain


def main():
    with open("input.txt", "r") as f:
        drawn_numbers = [int(n) for n in f.readline().split(",")]
        bingo_list = []
        bingo = []

        f.readline()  # remove next empty line

        for i, line in enumerate(f.readlines(), start=1):
            if i % 6 == 0:
                bingo_list.append(bingo)
                bingo = []
            else:
                bingo.append([int(n) for n in line.strip().split(" ") if n])

        bingo_list.append(
            bingo
        )  # add the last one; (bcs of how modulo appending works)

    # part 1
    # for number in drawn_numbers:
    #     for card in bingo_list:
    #         mark_card(card, number)
    #         if check_card(card):
    #             print("WINNER", card, number)
    #             result = sum(filter(lambda x: x > 0, chain(*card))) * number
    #             print("Result", result)
    #             return None

    # part 2
    winners = []
    for number in drawn_numbers:
        for i, card in enumerate(bingo_list):
            if i in winners:
                continue
            mark_card(card, number)
            if check_card(card):
                print(f"WINNER: bingo_list[{i}], {number=}")
                result = sum(filter(lambda x: x > 0, chain(*card))) * number
                print("Result", result)
                winners.append(i)
    print("Part 2^^^^^^^^^")  # last printed result is the part 2 solution


def mark_card(card: list[list[int]], number: int) -> None:
    """Marked number is replaced by -1"""
    for y in range(5):
        for x in range(5):
            if card[y][x] == number:
                card[y][x] = -1


def check_card(card: list[list[int]]) -> bool:
    # TODO cleanup two loops later
    """
    Check if all numbers in column or row are 'marked'

    See 'mark_card' function to check what 'marked' means
    """
    for row in card:
        if sum(row) == -5:
            return True

    # To check columns; transpose matrix and run loop again
    card = list(zip(*card))

    for row in card:
        if sum(row) == -5:
            return True

    return False


if __name__ == "__main__":
    main()
