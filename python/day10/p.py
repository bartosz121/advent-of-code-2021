input = [line.strip() for line in open("input.txt", "r")]

chars_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def get_points(c: str, part2: bool = False) -> int:
    """
    part 1:
    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.

    part 2:
    ): 1 point.
    ]: 2 points.
    }: 3 points.
    >: 4 points.

    """
    if part2:
        match c:
            case ')':
                return 1
            case ']':
                return 2
            case '}':
                return 3
            case '>':
                return 4
            case _:
                raise ValueError(f"get_point({c})")

    match c:
        case ')':
            return 3
        case ']':
            return 57
        case '}':
            return 1197
        case '>':
            return 25137
        case _:
            raise ValueError(f"get_point({c})")


def main():
    closing_chars = chars_map.values()
    part1_score = 0
    part2_score_list = []

    for line in input:
        chars = [] # or deque
        part2_line_score = 0

        for i, c in enumerate(line):
            if not chars:
                chars.append(c)
                continue

            if c in closing_chars:
                if chars_map[chars[-1]] != c:
                    part1_score += get_points(c)
                    break
                else:
                    chars.pop()
            else:
                chars.append(c)

            # part 2
            if i == len(line) - 1:
                chars.reverse() # have to because of the multiplication

                for c in chars:
                    closing_char = chars_map[c]
                    part2_line_score *= 5
                    part2_line_score += get_points(closing_char, part2=True)
                part2_score_list.append(part2_line_score)


    part2_score_list.sort()
    part2_score = part2_score_list[len(part2_score_list)//2]

    print(f"{part1_score=}")
    print(f"{part2_score=}")

if __name__ == "__main__":
    main()
