def hangman(word):
    wrong = 0
    stages = ["",
              "________",
              "|       |       ",
              "|       |       ",
              "|       0       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "              
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    print("Welcome to Hangman.")


    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a Charactor!"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
    
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win.")
            print(" ".join(board))
            win = True
            break
    
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose. The Anser is ...{}".format(word) )
        
import random
word_list = ["cat", "dog", "bird", "rabbit", "tortoise"]
word = word_list[random.randint(0, len(word_list) - 1)]
hangman(word)