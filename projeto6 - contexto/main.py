import openai

# A chave secreta da API da OpenAI
openai.api_key = '<YOUR API>'

# O histórico de chat inicialmente vazio
chat_history = []

def ask_question(question):
    # Adicione a nova pergunta ao histórico de chat
    chat_history.append({'user': question})

    # Formate o histórico de chat como um prompt para a API
    prompt = "\n".join([f"Usuário: {turn['user']}\nChatbot: {turn.get('bot', '')}" for turn in chat_history])

    # Adicione a nova pergunta ao prompt
    prompt += f"\nUsuário: {question}\nChatbot: "

    # Faça a chamada para a API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )

    # Adicione a resposta ao histórico de chat
    chat_history[-1]['bot'] = response.choices[0].text.strip()

    return response.choices[0].text.strip()

# Exemplo de uso
print(ask_question("Olá, como você está?"))
print(ask_question("Qual é a previsão do tempo para amanhã?"))
