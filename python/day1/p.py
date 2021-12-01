input = [int(line.strip()) for line in open("input.txt", "r")]

# input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


# part 11
# def main():
#     counter = 0
#     for i in range(1, len(input)):
#         if input[i] > input[i - 1]:
#             counter += 1

#     print(counter)


def main():
    measurments = []
    for i in range(len(input)):
        measurments.append(sum(input[i : i + 3]))

    print(measurments)

    counter = 0
    for i in range(1, len(measurments)):
        if measurments[i] > measurments[i - 1]:
            print(f"{measurments[i]} > {measurments[i - 1]}")
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
