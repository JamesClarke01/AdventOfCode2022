


def main():
    input = open("input.txt")

    total = 0

    for line in input:
        line = line.strip("\n")
        lineList = line.split(",")

        range1 = lineList[0].split("-")
        range2 = lineList[1].split("-")

        range1Start = int(range1[0])
        range1End = int(range1[1])

        range2Start = int(range2[0])
        range2End = int(range2[1])

        #if any point of range1 is within the bounds of range 2
        for point in range(range1Start, range1End+1):
            if point >= range2Start and point <= range2End:
                total += 1
                break
        
    print(total)


if __name__ == "__main__":
    main()