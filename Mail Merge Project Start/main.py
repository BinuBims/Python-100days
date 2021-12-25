#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from os import read


with open("Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()

name_list = []
with open("Input/Names/invited_names.txt") as names:
    names = names.read()
    for name in names.split("\n"):
        name_list.append(name)

for name in name_list:
    with open("Input/Letters/starting_letter.txt") as letter:
        letter = letter.read()
        ready_letter = letter.replace("[name]",name)
        print(ready_letter)
        with open(f"Output/ReadyToSend/{name}.txt", mode="w") as ready_let:
            ready_let.write(ready_letter)
