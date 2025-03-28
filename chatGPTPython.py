import requests
import time
import sys

with open('skChatGPT.txt','r') as key:
    data = key.read().strip()

api_key = data
model="text-davinci-003"

def chat_with_chatgpt(prompt):
    res = requests.post(f"https://api.openai.com/v1/completions",
          headers = {
              "Content-Type": "application/json",
              "Authorization": f"Bearer {api_key}"
          },
          json={
              "model": model,
              "prompt": prompt,
              "max_tokens": 100
          }).json()

    return res['choices'][0]['text'][1:]

while True:
    prompt = input('\n\nDuddits: ')
    if prompt == "done":
        break
    response = chat_with_chatgpt(prompt)
    print("Chatgpt Duddits responds",end='\n')

    for i in response:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.09)