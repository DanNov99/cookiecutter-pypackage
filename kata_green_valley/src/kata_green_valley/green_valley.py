def make_valley(l: list[int]):
    if not isinstance(l, list):
        return -1

    if len(l) <= 0:
        return -1

    for item in l:
        if not isinstance(item, int):
            return -1

    l.sort(reverse=True)
    left, right, valley = [], [], []

    for index, item in enumerate(l):
        if index % 2 == 0:
            left.append(item)
        else:
            right.append(item)

    valley.extend(left)
    valley.extend(reversed(right))

    return valley
