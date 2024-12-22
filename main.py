import openai
from personalities import personalities


openai.api_key = "Insert your OpenAI API key"


def generate_personality_response(user_input, conversation_history, personality="friendly"):

    system_message = {"role": "system", "content": personalities.get(personality, "You are an friendly assistant")}

    messages = [system_message] + conversation_history

    messages.append({"role":"user","content":user_input})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.9,
            max_tokens=150
        )

        ai_response = response['choices'][0]['message']['content'].strip()

        conversation_history.append({"role":"assistant", "content": ai_response})

        return ai_response
    
    except openai.error.InvalidRequestError as e:
        return f"Error: {str(e)}"
    

def start_conversation():
    conversation_history = []
    personality = "friendly"

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("conversation ended")
            break

        ai_reponse = generate_personality_response(user_input, conversation_history, personality)

        print(f"{ai_reponse}")

start_conversation()