# import random
from random import choice

# 1. You will store your poem in a .txt file. Feel free to use any poem of your choice!

# 2. Create a function called get_file_lines():

#     -It should have 1 parameter called filename, which is a string of the filename.
#     -It should return a list of strings containing the lines of the file.


def get_file_lines(filename):
    # input_file_name = filename
    infile = open(filename, 'r')
    lines_list = infile.readlines()
    infile.close()
    return lines_list

# 3. Create a function called lines_printed_backwards():

#     -It should have 1 parameter called lines_list, which is a list of strings containing lines of your poem.
#     -It should print the lines of the poem in reverse. Include the original line number at the beginning of each line.


def lines_printed_backwards(lines_list):
    lines_list.reverse()
    lines_length = len(lines_list)
    for i in range(lines_length):
        line = lines_list[i]
        line_number = lines_length - i
        print(f"{line_number} {line}")


lines_list = get_file_lines("poem.txt")
lines_printed_backwards(lines_list)

# 4. Create a function called lines_printed_random():

#     -It should have 1 parameter called lines_list, which is a list of strings containing lines of your poem.
#     -It should print the lines of your poem in random order. Repeats are ok, but make sure the number of lines
#     printed is equal to the original lines in the poem (Line numbers do not need to be printed.) Hint: try
#     using a loop and randint() from the random module.


def lines_printed_random(lines_list):
    # lines_length = len(lines_list)
    for i in range(len(lines_list)):
        print(choice(lines_list))


random_poem = get_file_lines('poem.txt')
lines_printed_random(random_poem)

# 5. Create a function called lines_printed_custom():

#     -It should minimally have 1 parameter called lines_list, which is a list of strings containing lines of your poem.
#     -It should print the poem in a unique way, be creative!
#     -Make sure that you carefully comment your custom function so it’s clear what it does.


def lines_printed_custom(lines_list):
    for line in lines_list:
        words = line.split(" ")
        print(words[0])


lines_printed_custom(lines_list)

# 6. Your final submitted code should use the four functions(get_file_lines(), lines_printed_backwards(), lines_printed_random(),
#    and lines_printed_custom()) you wrote. It should print out the poem contained in your text file backwards, random, and
#    custom to the terminal.


# Collaborative with Sawyer, Liz, Lon and Joi.
