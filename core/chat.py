import openai



def use(prompt,key):
    openai.api_key=key
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role":"user","content":prompt}
        ]
    )
    return response['choices'][0]['message']['content']

