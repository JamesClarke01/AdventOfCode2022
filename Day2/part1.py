
SCISSORS = "scissors"
ROCK = "rock"
PAPER = "paper"


decoderDict = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

shapeScoreDict = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS:3
}

#scoring
WIN_SCORE = 6
DRAW_SCORE = 3
LOSS_SCORE = 0


def gameOutcome(userChoice, elfChoice):
    
    outcomeScore = 0

    if(userChoice == ROCK and elfChoice == SCISSORS): #rock beats scissors
        outcomeScore = WIN_SCORE

    elif(userChoice == SCISSORS and elfChoice == PAPER): #scissors beats paper
        outcomeScore = WIN_SCORE

    elif(userChoice == PAPER and elfChoice == ROCK): #paper defeats rock
        outcomeScore = WIN_SCORE

    elif userChoice == elfChoice: #draw
        outcomeScore = DRAW_SCORE

    else:  #loss
        outcomeScore = LOSS_SCORE

    return outcomeScore


def main():

    input = open("input.txt", "r")

    totalScore = 0

    for line in input:
        
        line = line.strip("\n")
        lineList = line.split(" ")
        elfChoice = decoderDict[lineList[0]]
        userChoice = decoderDict[lineList[1]]
        
        outcomeScore = gameOutcome(userChoice, elfChoice)

        shapeScore = shapeScoreDict[userChoice]

        totalScore += outcomeScore + shapeScore

    print(totalScore)


if __name__ == "__main__":
    main()
