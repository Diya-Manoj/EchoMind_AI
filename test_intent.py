from utils.intent_detector import predict_intent

print("Type 'exit' to stop the chatbot.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot stopped.")
        break

    intent = predict_intent(user_input)

    print("Predicted Intent:", intent)