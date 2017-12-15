# PyChat 2K17

import random

def start():
    print(" _____ _      _   __  ___  __")
    print("/ ____(_)    (_) /_ |/ _ \\/_ |")
    print(" (___  _ _ __ _   | | | | || |")
    print("\___ \\| | '__| |  | | | | || |")
    print("____) | | |  | |  | | |_| || |")
    print("_____/|_|_|  |_|  |_|\\___/ |_|")
    
                                
    
def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        word  = " " + word
        if word in statement:
            return True

    return False

def get_question_response():
    responses = ["I don't know. What do you think?",
                 "I have no idea.",
                 "Huh?"]
    return random.choice(responses) 
    
def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?",
                 "None of your business.",
                 "Can we change the subject?"]

    return random.choice(responses)

            
def get_response(statement):
    statement = statement.lower()
    
    family_words = [" mother", "father", "brother", "sister", "mom", "dad", "cousin"]
    teacher_words = ["cooper", "class", " period", " computers"]
    animal_words = ["whale", "dog", "cat", "bird", "horse", "hamster"]
    color_words = ["blue", "red", "yellow", "green", "black", "white", "purple", "pink"]
    

    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, animal_words):
        response = "Tell me more about your pet."
    elif has_keyword(statement, color_words):
        response = ("That is a pretty. My favorite color is green.")
    else: 
        response = get_random_response()

    return response
    

mean_words_1= "shut up"
mean_words_2 = "you are annoying"
mean_words_3 = "you are boring" 

def play():
    talking = True

    print("Hello. I'm Siri101.")
    print("What is your name?")
    name = input("name: ")
    print("Hi " + name + "! " + "Say something to me!")

    while talking:
        statement = input(">> " + name + ": ")
    
        if statement == "Goodbye":
            talking = False
        elif statement == mean_words_1:
            print("That's mean. I do not want to talk to you anymore.") 
            talking = False
        elif statement == mean_words_2:
            print("That's mean. I do not want to talk to you anymore.") 
            talking = False
        elif statement == mean_words_3:
            print("That's mean. I do not want to talk to you anymore.") 
            talking = False

        else:
            response = get_response(statement)
            print(response)

    print("Goodbye.")

start()

playing = True

while playing:
    play()
    if mean_words_1:
        playing = False
    if mean_words_2:
        playing = False
    if mean_words_3:
        playing = False
    else:
        playing = confirm("Would you like to chat again?")

end()
