input = open("input.txt", "r")

mostElfCal = 0
currentElfCal = 0

for line in input:
    if line == "\n": #all else inventory has been checked, compare
        print("Current elf calories: ", currentElfCal)
        
        if currentElfCal > mostElfCal:  #check if this elf has more than the current highest
            mostElfCal = currentElfCal
            print("Elf with the most calories has: ", mostElfCal)
        
        currentElfCal = 0
        
    else:
        currentElfCal += int(line.strip("\n"))


print(mostElfCal)