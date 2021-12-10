input = [line.strip() for line in open("input.txt", "r")]

def decode_signals(signals: list[str]) -> dict[int, set[str]]:
    """https://old.reddit.com/r/adventofcode/comments/rc0ucn/2021_day_8_part_2_my_logic_on_paper_based_on_sets/"""
    map_: dict[int: set[str]] = dict()

    signals = sorted(signals, key=len) # sort by len, thats how i know which indexes to use below

    # 0's bcs indexes are changing after each pop
    map_[1] = set(signals.pop(0))
    map_[7] = set(signals.pop(0))
    map_[4] = set(signals.pop(0))
    map_[8] = set(signals.pop(-1))


    signals.reverse() # reverse because i need map_[6] to be present while doing len(5)

    for signal in signals:
        # Length 6 - (0, 6, 9)
        if len(signal) == 6:
            if map_[4].issubset(signal):
                map_[9] = set(signal)
            elif map_[7].issubset(signal):
                map_[0] = set(signal)
            else:
                map_[6] = set(signal)
        # Length 5 - (2, 3, 5)
        elif len(signal) == 5:
            if map_[7].issubset(signal):
                map_[3] = set(signal)
            elif map_[6].issuperset(signal):
                map_[5] = set(signal)
            else:
                map_[2] = set(signal)
        else:
            raise ValueError(signal, signals, map_)

    return map_



def get_digit(code: str, map_: dict[str, set[str]]) -> int:
    code_len = len(code)

    match code_len:
        # 1, 4, 7, 8 have unique length; no need to check with map
        case 2:
            return 1
        case 3:
            return 7
        case 4:
            return 4
        case 7:
            return 8
        case 6:
            candidates = (0, 6, 9)
            for candidate in candidates:
                # print(f"{code=} {candidate=} {[c in map_[candidate] for c in code]}")
                if all((c in map_[candidate] for c in code)):
                    return candidate
        case 5:
            candidates = (2, 3, 5)
            for candidate in candidates:
                # print(f"{code=} {candidate=} {[c in map_[candidate] for c in code]}")
                if all((c in map_[candidate] for c in code)):
                    return candidate
        case _:
            raise ValueError(code, code_len)


def main():
    part_1 = 0
    part_2 = 0
    for x in input:
        signals, output_values = x.split("|")
        signals = signals.split()
        output_values = output_values.split()

        part_1 += sum(1 for i in output_values if len(i) in (2, 4, 3, 7))


        # part 2
        digits_map = decode_signals(signals)
        output = ""

        for output_digit in output_values:
            output += str(get_digit(output_digit, digits_map))

        part_2 += int(output)

    print(part_1)
    print(part_2)


if __name__ == "__main__":
    main()
