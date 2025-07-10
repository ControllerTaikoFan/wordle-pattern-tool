dictionary = [] 
solution_word = ""
solution_word_lc = {}
pattern = [ 
    "_____",
    "_X_X_",
    "_____",
    "X___X",
    "_XXX_"
]
all_yellows = False

with open("dictionary/dictionary.txt") as file: # import dictionary
    for line in file:
        dictionary.append(line.rstrip())

solution_word = input("Input the solution word. ").lower().strip()
while (True):
    if (len(solution_word) != 5):
        solution_word = input("\nWord must be 5 letters. ").lower().strip()
        continue

    break

yellow_input = input("\nAll yellows? (y/n) ")
while (True):
    yellow_input = yellow_input.lower().strip()
    if (yellow_input != "y" and yellow_input != "n"):
        yellow_input = input("Must be either y or n ").lower().strip()
        continue

    if (yellow_input == "y"):
        all_yellows = True
        break
    elif (yellow_input == "n"):
        break

for letter in solution_word: # get letter count for solution word
    if (letter in solution_word_lc):
        solution_word_lc[letter] += 1
    else:
        solution_word_lc[letter] = 1

solution = []

def check(orientation):
    
    found_word = "none"
    for word in dictionary:
        if (word == solution_word):
            continue
        
        found_word_lc = {}     
        valid = True
        for i in range(5):
            letter = word[i]
            character_included = orientation[i] == "X"
        
            if ((letter in solution_word) != character_included): # check if the current letter is supposed to be solved or not
                valid = False
                break

            if (letter in solution_word and all_yellows): # check for all yellows
                if (letter == solution_word[i]):
                    valid = False
                    break
            
            if (letter in found_word_lc): # update letter count
                found_word_lc[letter] += 1
            else:
                found_word_lc[letter] = 1

            
            if (letter in solution_word_lc): # check for letter counts being greater than the solution word
                if (found_word_lc[letter] > solution_word_lc[letter]):
                    valid = False
                    break
                
                
        
        if (valid):
            found_word = word
            break
    return found_word


for i in pattern:
    found_word = check(i)
    if (found_word == "none"):
        print("\nNo solutions found")
        solution = []
        break
    solution.append(found_word)


if (len(solution) > 0):
    print("\nsolution:")
    for j in solution:
        print(j)


continue_input = input("\nMake a pattern line by line? (y/n) ")

if (continue_input == "y"):
    while (True):
        stop = False
        while (True):
            pattern = input("\nWhat's the pattern? (capital X to indicate a filled in square, _ for a grey type exit to exit) ")
            if (pattern.lower().strip() == "exit"):
                stop = True
                break
            if (len(pattern) != 5):
                print("Pattern must be 5 characters.")
            else:
                break
        if (stop):
            break


        yellow_input = input("All yellows? (y/n) \n")
        while (True):
            yellow_input = yellow_input.lower().strip()
            if (yellow_input != "y" and yellow_input != "n"):
                yellow_input = input("Must be either y or n ")
                continue

            if (yellow_input == "y"):
                all_yellows = True
                break
            elif (yellow_input == "n"):
                break

        found_word = check(pattern)
        if (found_word == "none"):
            print("\nNo word found")
        else:
            print(found_word)
        
input("\nPress enter to exit")

