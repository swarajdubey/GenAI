import requests
import json

#llama 3.2 was setup on this mac via ollama so need to call it here
user_input = "i like fresh air."
relevant_document = "Take a leisurely walk in the park and enjoy the fresh air."

prompt = """
You are a bot that makes recommendations for activities. Your answer is comprehensive with reasoning but concise and do not include any extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input
"""

url = "http://localhost:11434/api/generate" #Ollama by default runs on this URL

data = {
    "model":"llama3.2",
    "prompt": prompt.format(user_input=user_input,relevant_document=relevant_document)
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url,data=json.dumps(data),headers=headers,stream=True)
full_response = []

try:
    for line in response.iter_lines():
        if line:
            decoded_line = json.loads(line.decode('utf-8'))
            full_response.append(decoded_line['response'])
except:
    print("URL call failed")

response.close()
print(''.join(full_response))
