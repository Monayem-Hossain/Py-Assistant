import os
logo="""    _    _
   / \  | | _____  __
  / _ \ | |/ _ \ \/ /
 / ___ \| |  __/>  <
/_/   \_\_|\___/_/\_\ Your Py Assistant"""

B = '\033[34m'
C = '\033[36m'
# Define a dictionary of questions and their corresponding answers
qa_dict = {
    "what is your name": "My Name is Alex.",
    "tumar nam ki": "amar nam Alex.",
    "tumi ki korte paro": "ami sudu matro question er answer dite pari",
    "what can you do": "I can only answer some question .",
    "how old are you": "I am an AI language model, so I don't have an age.",
    "What is the capital of France": "The capital of France is Paris.",
    "Who is the president of the United States": "The president of the United States is Joe Biden.",
    "What is the meaning of life": "The meaning of life is subjective and varies from person to person.",
    "hi": "Hello sir!",
    "hlw": "Hi sir!",
    "how are you": "I am fine , sir! Thanks for asking.",
    "where are you now?": "Now i am in your phone. I don't know where i will be in future.",
    "who am i": "You don't know who you are ! Than how will i know ?🤣🤣",
    "Who am i": "You are Monayem , Sir.",
    "who made you": "I was made by Monayem Hossain.",
    "who are you": "I am Alex. Your Py assistant."
    
    # Add more questions and answers as needed
}
os.system("clear")
print(logo)

print("\n \n \n ")
# Loop to continuously ask questions and get answers
while True:
    question = input(""+B+"User: ")
    if question.lower() == 'exit':
        # Exit the loop when user types 'exit'
        break
    answer = qa_dict.get(question, "I don't know the answer to that question.\n  Please update my database.")
    print(""+C+"Alex:", answer)
    
##This project is made by Monayem Hossain .