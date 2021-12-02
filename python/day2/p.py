input = [line.strip() for line in open("input.txt", "r")]


# part 1
# def main():
#     depth = 0
#     h_pos = 0  # horizontal position

#     for l in input:
#         command, val = l.split()
#         val = int(val)
#         match command:
#             case 'forward':
#                 h_pos += val
#             case 'up':
#                 depth -= val
#             case 'down':
#                 depth += val
#             case _:
#                 raise ValueError(command)

#     print(f"{h_pos * depth=}")

def main():
    depth = 0
    h_pos = 0  # horizontal position
    aim = 0

    for l in input:
        command, val = l.split()
        val = int(val)
        match command:
            case 'forward':
                h_pos += val
                depth += aim * val
            case 'up':
                aim -= val
            case 'down':
                aim += val
            case _:
                raise ValueError(command)

    print(f"{h_pos * depth=}")

if __name__ == "__main__":
    main()
