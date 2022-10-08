import random

wordList = ["leblebi", "kelbetin"]
chosenWord = random.choice(wordList)
wordLength = len(chosenWord)

display = []
for i in range(wordLength): 
    display += "_"
print(display)

lives = 6
end_of_the_game = False
while not end_of_the_game :
    guess = input("enter the letter\n").lower()
    for position in range(wordLength) :
        letter = chosenWord[position] 
        if letter == guess :
            display[position] = letter
            
    
    if guess not in chosenWord:
        lives -=1
        print(f"WRONG U have {lives} attempts")
        if lives ==0:
            end_of_the_game = True
            print("You lose.")
            print(f"Word is {chosenWord}")
    
    print(display)
    
    if "_" not in display:
        end_of_the_game = True
        print("You win")



