'''
CS HW 7-19
'''

scrabble = input("Enter your Scrabble word: ")

def scrabble_score(word):
    word = word.lower()
    letter_scores = {1:
                     ["a","e","i","o","u","n","r","s","l","t"],
                     2:["g","d"],
                     3:["b","c","m","p"],
                     4:["f","h","v","w","y"],
                     5:["k"],
                     6:[],
                     7:[],
                     8:["j","x"],
                     9:[],
                     10:["q","z"]}
    total = 0
    for letter in word:
        for i in range(1, 11):
            if letter in letter_scores[i]:
                total += i
    print(total)

scrabble_score(scrabble)
                     
