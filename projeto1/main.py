import openai

openai.api_key = "<YOUR KEY>"

result = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is the distance between earth and mars?" }]
)

print(result)