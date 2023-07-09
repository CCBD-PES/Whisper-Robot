import openai

openai.api_key = "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"

model_engine = "gpt-3.5-turbo"
prompt = "Hello, how are you??"

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    temperature=0.5,
    stop=None,
)

print(response)