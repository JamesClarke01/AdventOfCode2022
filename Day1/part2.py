input = open("input.txt", "r")

top3 = []
currentElfCal = 0

for line in input:
    if line == "\n": #all elf inventory has been checked, compare
        print("Current elf calories: ", currentElfCal)
        
        if len(top3) < 3: #add fist 3 elves to list
                top3.append(currentElfCal)
                top3.sort()
                print("New top 3: ", top3)
        
        elif currentElfCal > top3[0]:  #check if this elf has more than the first elf in list
            
            top3[0] = currentElfCal
            top3.sort()
     
            print("New top 3: ", top3)
        
        currentElfCal = 0
        
    else: #increase current elf calory count
        currentElfCal += int(line.strip("\n"))



print(sum(top3))