


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

        
        if range1Start >= range2Start and range1End <= range2End: #if first range in second range
            total += 1
        elif range2Start >= range1Start and range2End <= range1End: #second range in in first range
            total += 1

    print(total)






if __name__ == "__main__":
    main()