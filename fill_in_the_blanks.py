easy = "Easy difficulty level selected!\n"
medium = "Medium difficulty level selected!\n"
hard = "Hard difficulty level selected!\n"
greet = "Thank you for being awesome and playing my game! Now, let's start playing the game, shall we?"
correct = "That's is the correct answer, good job!"
incorrect = "I'm sorry, but that's not the answer we are looking for, please try again."
user_input = ""

easy_sentence = "The Python programming language was first released in the 'BLANK' 1991. Has a design philosophy that emphasizes code 'BLANK'. The creator's country of origin is 'BLANK', his name is 'BLANK'."
medium_sentence = "Hypertext Markup Language acronym is 'BLANK', and is the standard markup language for creating 'BLANK' and 'BLANK'. With Cascading Style Sheet, which the acronym is 'BLANK', and 'BLANK' it forms a triad of conerstone technologies for the World Wide Web. HTML 'BLANK' are the building blocks of HTML pages."
hard_sentence = "Cascading Style Sheet is a style sheet language used for describing the 'BLANK' of a document written in a 'BLANK' language. Although most often used to set the visual style of web pages and user interfaces written in 'BLANK' and 'BLANK'. Along with HTML and 'BLANK', CSS is a cornerstone technology used by most 'BLANK' to create visually engaging webpages, user interfaces for web 'BLANK', and user interfaces for many 'BLANK' applications."

easy_answers = ["year", "readability", "the netherlands", "guido van rossum"]
medium_answers = ["html", "web pages", "web applications", "css", "javascript", "elements"]
hard_answers = ["presentation", "markup", "html", "xhtml", "javascript", "websites", "applications", "mobile"]

user_easy_answers = []
user_medium_answers = []
user_hard_answers = []

###----Difficulty validator. Takes user input and checks what difficulty has been selected.----###
def diff_validation():
    user_input= raw_input("Welcome to 'Fill in the Blanks!'\n\nPlease select the difficulty level (easy, medium or hard): ").lower()
    while True:
        if user_input == "easy" or user_input == "medium" or user_input == "hard":
            return user_input
        else:
            print "Please select a valid difficulty level between 'easy', 'medium' and 'hard'"
            user_input= raw_input("\nType your answer, case sensitive (easy, medium or hard): ")

###----At this point the game difficulty has been selected and the input validated. This procedure launches the game corresponding to the user selection. Takes as input the difficulty selected.----####
def game(diff):
    if diff == "easy":
        print easy
        easy_diff()
    elif diff == "medium":
        print medium
        medium_diff()
    elif diff == "hard":
        print hard + "Hope you are ready!\n" + "\nThis is your sentence, please do the best on filling the 'BLANKS'.\n"
        hard_diff()
        ###ADD THE CODE FOR THE HARD PART---------------

###----This definition finds the starting index of the word passed as an input, in our case, BLANK. After it has been found, it returns a list with the index numbers of the word passed starting point.----###
def word_find(s, r, start=0):
    if start >= len(s):
        return []
    if s.startswith(r, start):
        return [start] + word_find(s, r, start+1)
    else:
        return word_find(s, r, start+1)

###----This procedure initiates the game on the easy difficulty.----###
def easy_diff():
    print easy_sentence + "\nThis is your sentence, please do the best on filling the 'BLANKS'.\n"
    list1 = word_find(easy_sentence, "BLANK")
    easy_concatenated(list1)

###----This procedure initiates the game on the medium difficulty.----###
def medium_diff():
    print medium_sentence + "\nThis is your sentence, please do the best on filling the 'BLANKS'.\n"
    list2 = word_find(medium_sentence, "BLANK")
    medium_concatenated(list2)

###----This procedure initiates the game on the hard difficulty.----###
def hard_diff():
    print hard_sentence + "\nThis is your sentence, please do the best on filling the 'BLANKS'.\n"
    list3 = word_find(hard_sentence, "BLANK")
    hard_concatenated(list3)

##----Concatenates the sentence using a list (input) of the index positions of the word being replaced, in our case, the 'BLANKS'.----##
def easy_concatenated(list1):
    easy_string = easy_sentence
    first_ans = raw_input("Please enter the first answer: ").lower()
    easy_answer_validation(first_ans)
    first = easy_string[:list1[0]] + user_easy_answers[0].title()
    second_ans = raw_input("Please enter the second answer: ").lower()
    easy_answer_validation(second_ans)
    second = easy_string[list1[0]+5:list1[1]] + user_easy_answers[1].title()
    third_ans = raw_input("Please enter the third answer: ").lower()
    easy_answer_validation(third_ans)
    third = easy_string[list1[1]+5:list1[2]] + user_easy_answers[2].title()
    fourth_ans = raw_input("Please enter the fourth answer: ").lower()
    easy_answer_validation(fourth_ans)
    fourth = easy_string[list1[2]+5:list1[3]] + user_easy_answers[3].title()
    fifth = easy_string[list1[3]+5:]
    new_sentence1 = first + second + third + fourth + fifth
    print "\n" + new_sentence1
    victory()

##----Concatenates the sentence using a list (input) of the index positions of the word being replaced, in our case, the 'BLANKS'.----##
def medium_concatenated(list2):
    medium_string = medium_sentence
    first_ans = raw_input("Please enter the first answer: ").lower()
    medium_answer_validation(first_ans)
    first = medium_string[:list2[0]] + user_medium_answers[0].title()
    second_ans = raw_input("Please enter the second answer: ").lower()
    medium_answer_validation(second_ans)
    second = medium_string[list2[0]+5:list2[1]] + user_medium_answers[1].title()
    third_ans = raw_input("Please enter the third answer: ").lower()
    medium_answer_validation(third_ans)
    third = medium_string[list2[1]+5:list2[2]] + user_medium_answers[2].title()
    fourth_ans = raw_input("Please enter the fourth answer: ").lower()
    medium_answer_validation(fourth_ans)
    fourth = medium_string[list2[2]+5:list2[3]] + user_medium_answers[3].title()
    fifth_ans = raw_input("Please enter the fifth answer: ").lower()
    medium_answer_validation(fifth_ans)
    fifth = medium_string[list2[3]+5:list2[4]] + user_medium_answers[4].title()
    sixth_ans = raw_input("Please enter the sixth answer: ").lower()
    medium_answer_validation(sixth_ans)
    sixth = medium_string[list2[4]+5:list2[5]] + user_medium_answers[5].title()
    seventh = medium_string[list2[5]+5:]
    new_sentence2 = first + second + third + fourth + fifth + sixth + seventh
    print "\n" + new_sentence2
    victory()

##----Concatenates the sentence using a list (input) of the index positions of the word being replaced, in our case, the 'BLANKS'.----##
def hard_concatenated(list3):
    hard_string = hard_sentence
    first_ans = raw_input("Please enter the first answer: ").lower()
    hard_answer_validation(first_ans)
    first = hard_string[:list3[0]] + user_hard_answers[0].title()
    second_ans = raw_input("Please enter the second answer: ").lower()
    hard_answer_validation(second_ans)
    second = hard_string[list3[0]+5:list3[1]] + user_hard_answers[1].title()
    third_ans = raw_input("Please enter the third answer: ").lower()
    hard_answer_validation(third_ans)
    third = hard_string[list3[1]+5:list3[2]] + user_hard_answers[2].title()
    fourth_ans = raw_input("Please enter the fourth answer: ").lower()
    hard_answer_validation(fourth_ans)
    fourth = hard_string[list3[2]+5:list3[3]] + user_hard_answers[3].title()
    fifth_ans = raw_input("Please enter the fifth answer: ").lower()
    hard_answer_validation(fifth_ans)
    fifth = hard_string[list3[3]+5:list3[4]] + user_hard_answers[4].title()
    sixth_ans = raw_input("Please enter the sixth answer: ").lower()
    hard_answer_validation(sixth_ans)
    sixth = hard_string[list3[4]+5:list3[5]] + user_hard_answers[5].title()
    seventh_ans = raw_input("Please enter the seventh answer: ").lower()
    hard_answer_validation(seventh_ans)
    seventh = hard_string[list3[5]+5:list3[6]] + user_hard_answers[6].title()
    eight_ans = raw_input("Please enter the eight answer: ").lower()
    hard_answer_validation(eight_ans)
    eight = hard_string[list3[6]+5:list3[7]] + user_hard_answers[7].title()
    nine = hard_string[list3[7]+5:]
    new_sentence3 = first + second + third + fourth + fifth + sixth + seventh + eight + nine
    print "\n" + new_sentence3
    victory()

###----This module definitions validates the user answers by parsing the answers list corresponding to the difficulty and checking if it's correct. If the answer is incorrect, it will ask to try again.----###

def easy_answer_validation(answers):
    if answers in easy_answers:
        print "Correct!."
        user_easy_answers.append(answers)
    else:
        while answers not in easy_answers:
            print answers + " is not the correct answer, please try again."
            answers = raw_input("Please enter the corrrect answer: ").lower()
        user_easy_answers.append(answers)

###----This module definitions validates the user answers by parsing the answers list corresponding to the difficulty and checking if it's correct. If the answer is incorrect, it will ask to try again.----###
def medium_answer_validation(answers):
    if answers in medium_answers:
        print "Correct!."
        user_medium_answers.append(answers)
    else:
        while answers not in medium_answers:
            print answers + " is not the correct answer, please try again."
            answers = raw_input("Please enter the corrrect answer: ").lower()
        user_medium_answers.append(answers)

###----This module definitions validates the user answers by parsing the answers list corresponding to the difficulty and checking if it's correct. If the answer is incorrect, it will ask to try again.----###
def hard_answer_validation(answers):
    if answers in hard_answers:
        print "Correct!."
        user_hard_answers.append(answers)
    else:
        while answers not in hard_answers:
            print answers + " is not the correct answer, please try again."
            answers = raw_input("Please enter the corrrect answer: ").lower()
        user_hard_answers.append(answers)

###----Victory precedure, that informs the user of his victory and asks if the user wants to play again----###
def victory():
    again = raw_input("\nCongratulations! You have completed all the 'BLANKS'!!!. Would you like to play again?(Y/N): ")
    if again == "Y" or again == "y":
        game(diff_validation())
    elif again == "N" or again == "n":
        quit()

game(diff_validation())
