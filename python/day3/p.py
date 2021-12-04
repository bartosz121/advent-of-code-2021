input = [line.strip() for line in open("input.txt", "r")]


def part_2(*, fn) -> str:
    """Fn will be max/min (oxygen generator/co2)"""
    data = input.copy()

    current_bit = 0
    while len(data) > 1:
        counter = {"0": 0, "1": 0}
        for code in data:
            counter[code[current_bit]] += 1

        # edge case if 1's and 0's are equal
        if counter["0"] == counter["1"]:
            if fn.__name__ == "max":
                most_common = "1"
            else:
                most_common = "0"
        else:
            most_common = fn(counter, key=counter.get)
        data = list(filter(lambda x: x[current_bit] == most_common, data))
        # print(f"({fn=})({current_bit=}){most_common=}{counter=}{data=}")
        current_bit += 1

    return data[0]


def main():
    # part 1
    # part_1 = {}
    # for code in input:
    #     for i, c in enumerate(code):
    #         try:
    #             part_1[i][c] += 1
    #         except KeyError:
    #             part_1[i] = {"0": 0, "1": 0}
    #             part_1[i][c] += 1

    # # gamma
    # gamma = ""
    # for v in part_1.values():
    #     gamma += max(v, key=v.get)

    # # epsilon
    # epsilon = ""
    # for v in part_1.values():
    #     epsilon += min(v, key=v.get)

    # print(f"Part 1: {int(gamma, base=2) * int(epsilon, base=2)}")

    # part 2
    oxygen = part_2(fn=max)
    co2 = part_2(fn=min)

    print(f"{oxygen=} {co2=}")

    print(f"Part 2: {int(oxygen, base=2) * int(co2, base=2)}")


if __name__ == "__main__":
    main()
