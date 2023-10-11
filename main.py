import openai

openai.api_key = "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"

def chat_gtp(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}]
        )
    return response.choices[0].message.content.strip()

if __name__ == '__main__':
    while True:
        user_input = input("You: ")
        if user_input.lower() =="quit":
            break

        response = chat_gtp(user_input)
        print("Chatbot: ", response)