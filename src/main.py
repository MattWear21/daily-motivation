import requests
from ollama import chat
from ollama import ChatResponse
from dotenv import load_dotenv
import os

load_dotenv()
webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
model_name = os.getenv("OLLAMA_MODEL")

response: ChatResponse = chat(model=model_name, messages=[
  {
    'role': 'user',
    'content': 'Generate a single, short, motivational statement to be read by a user when they first wake up in the morning. Respond only with the motivational quote.',
  },
])
print(response['message']['content'])


summary = response['message']['content']
# Post message on Discord
requests.post(
    webhook_url,
    json={"content": summary}
)
print("Successfully posted to discord:", summary)
