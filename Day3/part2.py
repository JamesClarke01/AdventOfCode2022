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
    count = 0
    elfGroup = []

    for line in input:
        count += 1

        elfGroup.append(line.strip("\n"))

        if count % 3 == 0:

            elf1 = list(elfGroup[0])
            elf2 = list(elfGroup[1])
            elf3 = list(elfGroup[2])

            shared = None

            for i in elf1:
                for j in elf2:
                    if i == j:
                        for k in elf3:
                            if i == k:
                                shared = i
                                

            priority = getPriority(shared)

            total += priority

            elfGroup = []

    print(total)

if __name__ == "__main__":
    main()