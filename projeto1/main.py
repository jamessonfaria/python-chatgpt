import openai

openai.api_key = "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"

result = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": "What is the distance between earth and mars?" }]
)

print(result)