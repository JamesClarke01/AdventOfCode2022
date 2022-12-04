
def getPriority(character):
    unival = ord(character)
    priority = None

    if unival >= 97:
        priority = unival - 96
    elif unival >= 65:
        priority = unival - 38

    return priority


def main():
    input = open("input.txt", "r")

    total = 0

    for line in input:
        line = line.strip("\n")
        p1Str = line[0:int(len(line)/2)]
        pt2Str = line[int(len(line)/2):len(line)]

        p1List = list(p1Str)
        p2List = list(pt2Str)

        shared = None

        for i in p1List:
            for j in p2List:
                if i == j:
                    shared = i

        priority = getPriority(shared)

        total += priority

    print(total)

if __name__ == "__main__":
    main()