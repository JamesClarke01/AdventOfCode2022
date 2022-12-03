

SCISSORS = "scissors"
ROCK = "rock"
PAPER = "paper"
LOSE = "lose"
DRAW = "draw"
WIN = "win"

decoderDict = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}

shapeScoreDict = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS:3
}

conditionScoreDict = {
    WIN: 6,
    DRAW: 3,
    LOSE: 0
}


def gameOutcome(condition, elfChoice):
    
    shape = None
    
    if(elfChoice == SCISSORS): #rock beats scissors
        if condition == WIN: 
            shape = ROCK
        elif condition == LOSE:
            shape = PAPER
        elif condition == DRAW:
            shape = elfChoice
    
    elif(elfChoice == PAPER):
        if condition == WIN: 
            shape = SCISSORS
        elif condition == LOSE:
            shape = ROCK
        elif condition == DRAW:
            shape = elfChoice
    
    elif(elfChoice == ROCK):
        if condition == WIN: 
            shape = PAPER
        elif condition == LOSE:
            shape = SCISSORS
        elif condition == DRAW:
            shape = elfChoice

    return shape


def main():

    input = open("input.txt", "r")

    totalScore = 0

    for line in input:
        
        line = line.strip("\n")
        lineList = line.split(" ")
        elfChoice = decoderDict[lineList[0]]
        condition = decoderDict[lineList[1]]
        
        shape = gameOutcome(condition, elfChoice)

        shapeScore = shapeScoreDict[shape]

        totalScore += conditionScoreDict[condition] + shapeScore
      
    print(totalScore)



if __name__ == "__main__":
    main()
