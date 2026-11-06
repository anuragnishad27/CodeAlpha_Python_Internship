def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "I am a Python chatbot."

    elif user_input == "who created you":
        return "I was created by a Python programmer."

    elif user_input == "thank you":
        return "You're welcome!"
    elif user_input == "bye":
         return "Goodbye!"
    
    else:
        return "Sorry, I don't understand that."

def start_chatbot():
        print("============================")
        print("    WELCOME TO CHATBOT      ") 
        print("============================")
        print("Type 'bye' to exit the chatbot. \n")

        while True:
            user_input = input("You: ")
            
            response = chatbot_response(user_input)
            print("Bot:", response)

            if user_input.lower().strip() == "bye":
                break 

if __name__== "__main__":
    start_chatbot()
        