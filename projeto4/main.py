import openai

openai.api_key = "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"

audio_file = open("C:\work\pessoal\chatgpt\projetos-python\python-chatgpt\projeto4\/audio\german1.mp3", "rb")
result = openai.Audio.transcribe("whisper-1", audio_file)
print(result)

audio_file2 = open("C:\work\pessoal\chatgpt\projetos-python\python-chatgpt\projeto4\/audio\german1.mp3", "rb")
result2 = openai.Audio.translate("whisper-1", audio_file2)
print(result2)