import random

# Define some possible user inputs and corresponding chatbot responses
#left= audiance questions.
#right chat bot answer.

responses = {
              "hii"  :    "Hello!",
      "who are you"  :   "chatbot",
            "hello"  :    "Hi there!",
     "how are you?"  :    "I'm doing well, thanks for asking!",
 "what's your name?" :    "My name is ChatBot.",
            "bye"    :    "Goodbye!",
    "see you later"  :    "See you later!",
    "how to prepare for travel" :"pack all the necessary things.",
    "do you know my name": "yes",
}


# Define a function to handle user input and return the appropriate chatbot response
def respond(input_text):
    input_text = input_text.lower()
    for key in responses.keys():
        if key in input_text:
            return responses[key]
    return "I'm sorry, I don't understand what you're asking."

# Loop to continually accept user input and provide chatbot responses
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print(responses['bye'])
        break
    else:
        print("ChatBot:", respond(user_input))
