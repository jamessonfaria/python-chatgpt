import openai
from langchain.memory import ChatMessageHistory

openai.api_key = '<YOUR API>'

# Inicialize o histórico de mensagens
message_history = ChatMessageHistory()

def ask_question(question):
    # Adicione a pergunta do usuário ao histórico de mensagens
    message_history.add_user_message(question)

    # Gere uma resposta
    response = generate_response(message_history.messages)

    # Adicione a resposta da IA ao histórico de mensagens
    message_history.add_ai_message(response)

    return response

def generate_response(messages):
    # Extraia o conteúdo de cada mensagem e combine em uma única string
    context = " ".join(message.content for message in messages)

    # Use a API de completion da OpenAI para gerar uma resposta
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=context,
        max_tokens=150
    )

    return response.choices[0].text.strip()

# Exemplo de uso
print(ask_question("Qual é o tempo hoje?"))
print(ask_question("E amanhã?"))
print(ask_question("Qual é a previsão para a próxima semana?"))
print(ask_question("Vai chover?"))
print(ask_question("Eu preciso de um guarda-chuva?"))
