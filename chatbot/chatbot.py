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

        if answer in ["y" , "yes", "yup", "yeah"]:
            return True
        elif answer in ["n", "no", "nope", "nah"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        word  = " " + word
        if word in statement:
            return True

    return False

    
def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?",
                 "None of your business.",
                 "Can we change the subject?"]

    return random.choice(responses)

def get_answer():
    responses = ["I don't know", "Huh?", "I do not understand. My knowledge is limited because I am a primitive computer."]
    return random.choice(responses)
    
            
def get_response(statement):
    statement = statement.lower()
    
    family_words = ["mother", "father", "brother", "sister", "mom", "dad", "cousin", "family"]
    teacher_words = ["cooper", "class", " period", " computers"]
    animal_words = ["whale", "dog", "cat", "bird", "horse", "hamster"]
    color_words = ["blue", "red", "yellow", "green", "black", "white", "purple", "pink"]
    questions = ["what's up", "how are you", "how are you doing", "why am i talking to you"]
    positive_feelings = ["i am doing well", "i am happy", "delighted", "awesome"]
    negative_feelings = ["sad", "angry", "mad", "upset", "depressed"]
    agree_words = ["yes", "definitely", "yeah", "y", "agree"]
    disagree_words = ["no", "nope", "definitely not", "disagree"]
    changing_subject = ["can we change the subject", "i am tired of talking about this", "this is too intrusive"]
    

    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, animal_words):
        response = "Tell me more about your pet."
    elif has_keyword(statement, color_words):
        response = ("That is a pretty. My favorite color is green.")
    elif has_keyword(statement, questions):
        response = ("I do not know. I am a computer program after all. How are you doing?")
    elif has_keyword(statement, positive_feelings):
        response = ("That is good to hear. Tell me more about it.")
    elif has_keyword(statement, negative_feelings):
        response = ("That is unfortunate. Do you want to change the subject?")
    elif has_keyword(statement, agree_words):
        response = ("Ok, can you elaborate?")
    elif has_keyword(statement, disagree_words):
        response = ("Hmmm.... Why not?")
    elif statement [-1] == "?":
        response = get_answer()
    elif has_keyword(statement, changing_subject):
        response = ("We can talk about whatever you want to. After all, I am just a program.") 
    else: 
        response = get_random_response()
        
    return response
    

mean_words_1= "shut up"


def play():
    talking = True

    print("Hello. I'm Siri101.")
    print("What is your name?")
    name = input("name: ")
    print("Hi " + name + "! " + "Say something to me!")

    while talking:
        statement = input(">>> " + name + ": ")
    
        if statement == "Goodbye":
            print("Goodbye. It was nice talking to you, " + name)
            talking = False
        elif statement == mean_words_1:
            print("That's rude. I am not talking to you anymore " + name)
            talking = False
        else:
            response = get_response(statement)
            print(response)
    
start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")


end()
