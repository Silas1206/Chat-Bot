import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
def conversar_com_gpt():
    while True:
        user_input =input("voce: ")

        if user_input.lower()=="sair":
            print("ChatGPT  BOT: Tchau!")
            break
        completion = client.chat.completions.create(    
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
        ],
        
        model ="gpt-4o-mini",
    )
    reply = completion.choices[0].message.content

    print("ChatGPT BOT:", reply)
    
conversar_com_gpt()