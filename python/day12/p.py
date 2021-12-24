from collections import defaultdict, Counter
from typing import List

input = [line.strip() for line in open("input.txt", "r")]

map_ = defaultdict(list)

for p in input:
    v1, v2 = p.split("-")
    map_[v1].append(v2)
    map_[v2].append(v1)


def main():
    def search(path: List[str]) -> None:
        # print(f"search({path}) {path[-1]=} {map_[path[-1]]}")

        if path[-1] == "end":
            nonlocal result
            result += 1
            return None

        candidates: List[str] = map_.get(path[-1])

        # part 2
        counter = Counter(filter(lambda x: x.islower(), path))  # remove 'big caves'

        # part 2
        max_counter_value = max(counter.values())

        candidates = [x for x in candidates if x != "start"]

        # part 2
        for c in candidates:
            if c.isupper() or c not in path or max_counter_value < 2:
                p_copy = path.copy()
                p_copy.append(c)
                search(p_copy)

        # part 1
        # for c in candidates:
        #     if c not in path or c.isupper():
        #         p_copy = path.copy()
        #         p_copy.append(c)
        #         search(p_copy)

        return None

    result = 0
    for v in map_["start"]:
        search([v])

    print(f"{result=}")


if __name__ == "__main__":
    main()
