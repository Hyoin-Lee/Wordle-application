import random

# TODO: select target word at random from TARGET_WORDS
def get_target_word():  # Function that emulates a random word from a file
    with open("./word-bank/target_words.txt") as file:
        words = file.read()
    words_list = words.split("\n")
    return random.choice(words_list)

# TODO: ensure guess in VALID_WORDS
def get_valid_word():  # Function that loads all valid word
    with open("./word-bank/all_words.txt") as file:
        words = file.read()
    valid_words_list = words.split("\n")
    return valid_words_list

# TODO: provide clues for each character in the guess using your scoring algorithm
def guess(try_word): # Function that score for guess_word
    try_word = try_word.lower()
    answer_string = ["0", "0", "0", "0", "0"]
    print("guess : " + try_word)
    for index, value in enumerate(try_word):
        if (target_word[index] == value):
            answer_string[index] = "2"
        elif (value in target_word):
            answer_string[index] = "1"

    result = "".join(answer_string)   # list to string
    print(result)
    if (result == "22222"):
        return True
    else:
        return False


# main
valid_words_list = get_valid_word()
try_count = 6
target_word = get_target_word()

## print("target : " + target_word)
while True:
    if (try_count == 0):
        print("Sorry, You've run out of maximum try. Better luck next time!")
        break

    guess_word = input("Guess a 5-letter word: ")
    if (guess_word in valid_words_list):
        try_count = try_count - 1
        if (guess(guess_word)):
            print("Congratulation, You win")
            break
        else:
            print("try again")
    else:
        print("Please input valid word!")
