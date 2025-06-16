from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()
def chat_bot_logic(user_message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. You have a proper knowledge in machine learning. Give proper answer in a simple way"}, # <-- This is the system message that provides context to the model
            {"role": "user", "content": user_message}  # <-- This is the user message for which the model will generate a response
        ]
    )
    return response.choices[0].message.content
