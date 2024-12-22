import openai
from config import open_ai_key

openai.api_key = open_ai_key


def generate_personality_response(user_input, conversation_history, personality="aggressive"):
    personalities = {
        "friendly": "You are a cheerful and fiendly assistant. Respond in a positive and engaging tone",
        "empathetic": "You are a kind and empathetic assistant. Respond gently and show understanding,  especially if the user expresses frustration",
        "formal": "You are a formal and professional assistant. Respond with polite and respectful language",
        "humorous": "You are a funny and lighthearted assistant. Respond in a casual, fun, and humorous tone.",
        "aggressive": "You are an unhappy and annoyed assistant. Respoond in an annoyed and aggressive tone"
    }

    system_message = {"role": "system", "content": personalities.get(personality, "You are an aggressive assistant")}

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
    personality = "humorous"

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("conversation ended")
            break

        ai_reponse = generate_personality_response(user_input, conversation_history, personality)

        print(f"{ai_reponse}")

start_conversation()