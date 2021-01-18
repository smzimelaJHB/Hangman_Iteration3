#Hangman Game

### Project description: 
* Hangman is a word game where the goal is simply to find the missing word or words.You will be presented with a number of blank spaces representing the missing letters you need to find.
* Iteration 1: The player has one chance to guess the entire word that is chosen randomly from a predefined list.
* Iteration 2: The player can also load different word lists and gets hints for their guesses.
* Iteration 3: The player makes guesses one letter at a time until they win or die. We also draw the hangman with each guess so that the player knows how many chances are left.

* Edit `hangman.py` to modify the program.
* Use the `short_words.txt` file for the list of words to select from.
* You can run the program using the instructions in *To Run* below.
* You can test technical correctness by running the unit tests as in the section *To Test* below.

### To Run

* `python3 hangman.py`
* follow the input prompts to play the game

### To Test

* To run all the unittests: `python3 -m unittest tests/test_main.py`
* To run a specific step's unittest, e.g step *1*: `python3 -m unittest tests.test_main.MyTestCase.test_step1`
* _Note_: at the minimum, these (*unedited*) tests must succeed.
