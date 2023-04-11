import openai

openai.api_key = "<YOUR KEY>"

result = openai.Image.create(
    prompt = "An astronaut in yellow Hawaiian sandals on the moon with Batman's cape",
    n = 1,
    size = "1024x1024"
)

print(result)