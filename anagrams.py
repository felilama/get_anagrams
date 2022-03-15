import os
import time
import sys


def get_file():

    with open("sv-utf8.txt","r") as file:
        lexicon_dict = {} #dic created from lexicon
        content = file.read().lower().split()
        content_list = sorted(content)

        for i in range(0,len(content_list)):
            dic_lex[content_list[i]]=[]
            for z in range(0,len(content_list)):

                if len(content_list[i])==len(content_list[z]) and content_list[i] != content_list[z]:
                    if sorted(content_list[i])==sorted(content_list[z]):
                        print("anagram found")

                        lexicon_dict[content_list[i]].append(content_list[z])
        
    
def anagram():
   

    with open("sv-utf8.txt","r") as file:
        content = file.read().lower().split()
        content_list = sorted(content)
        lexicon_dict = {}
        input_word = input("Enter a word: ")
        
        lexicon_dict [input_word] = []
        if input_word in content_list:
            print("Word in lexicon")
            
            for i in range(0,len(content_list)):
                if len(input_word) == len (content_list[i]) and input_word != content_list[i]:
                    if sorted(content_list[i]) == sorted(input_word):
                        lexicon_dict[input_word].append(content_list[i])
            if len(lexicon_dict[input_word]) == 0:
                print("No anagrams found")
            else:
                print(lexicon_dict)
        else:
            print("Word not found")

        again = ask()
        if again:
            return anagram()
        print("Thanks for using the program!!!")

def ask():

    choice = input("Do you want to this again? | yes/no: ")
    if choice.lower() == "yes":
        return True
    elif choice.lower() == "no":
        return False
    print("Answer only yes or no please ")
    return ask()
              

                
if __name__ == "__main__":
    #get_file()
    anagram()
    #again = ask()
