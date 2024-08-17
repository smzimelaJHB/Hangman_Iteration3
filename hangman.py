import random
import sys
"""ts"""
def read_file(file_name):
    """Open file reading line by line, 
       Store results as a list
       close file and finally return list.
       """
    file = open(file_name,'r')
    f = file.readlines()
    file.close()
    return f


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    if file_name == "":
        return 'short_words.txt'
    else:
        return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word



def random_fill_word(word):
    """update to randomly fill in one character of the word only"""
    num = random.randint(0,len(word)-1)
    Temp = list("_"*len(word))
    Temp[num] = word[num]
    Result = "".join(Temp)
    return Result
    


def is_missing_char(original_word, answer_word, char):
    """update to check if character is one of the missing characters"""
    if(char in original_word and char not in answer_word):
        return True
    else:
        return False




def fill_in_char(original_word, answer_word, char):
    """fill in missing char in word and return new more complete word"""
    Temp = list(answer_word)
    Result = answer_word
    for i in range(len(answer_word)-1):
        if(original_word[i] == char and answer_word[i] == '_'):
            Temp[i] = char
            Result = "".join(Temp)
            break
    return Result


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


def do_wrong_answer(answer, number_guesses):
    """update to use number of remaining guesses"""
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


def draw_figure(number_guesses):
    """draw hangman stick figure, based on number of guesses remaining"""
    print("/----")
    n_g = 5 - number_guesses      #start from 1
    if(n_g == 1):
        for i in range(4):
            print('|')
    if(n_g == 2):
        print('|'+"   "+"0")
        for i in range(3):
            print('|')
    if(n_g == 3):
        print('|   0')
        print("|   |")
        print('|   |')
        print('|    ')
    if(n_g == 4):
        print('|   0')
        print('|   |')
        print('|   |')
        print('|  / \\')
    if(n_g == 5):
        print('|   0')
        print('|  /|\\')
        print('|   |')
        print('|  / \\')
    print("_______")







def run_game_loop(word, answer):
""""update to loop over getting input and checking until whole word guessed
    update loop to exit game if user types `exit` or `quit`
    keep track of number of remaining guesses""""
    print("Guess the word: "+answer)
    g = 5
    while True:
        if word == answer:
            break
        guess = get_user_input()
        if guess == 'exit' or guess == 'quit':
            print('Bye!')
            break
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        else:
            g = g - 1
            do_wrong_answer(answer, g)
            if g == 0:
                print("Sorry, you are out of guesses. The word was: "+str(word))
                break


if __name__ == "__main__":
    """update to get words_file to use from commandline argument"""
    if(len(sys.argv) == 1):
        file_name = ""
    else:
        file_name = sys.argv[1]

    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

