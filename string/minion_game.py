"""Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: ."""

def minion_game(string):
    vow="AEIOU"
    kevin=0
    stuart=0
    n=len(string)
    for i in range(n):
        if string[i] in vow:
            kevin+=n-i
        else:
            stuart+=n-i
    if kevin>stuart:
        print("Kevin", kevin)
    elif kevin==stuart:
        print("Draw")
    else:
        print("Stuart", stuart)

if __name__ == '__main__':
    s = input()
    minion_game(s)
