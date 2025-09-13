import requests
API_KEY = 'AIzaSyDauvBOZu_jYc-_XMmXTUVt8ACVPXATyVQ'
API_URL = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}'
def send_message(prompt):
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 200:
        response_data = response.json()
        generated_text = response_data['candidates'][0]['content']['parts'][0]['text']
        return generated_text
    else:
        # Print the error if something went wrong
        print(f"Error: {response.status_code} - {response.text}")
        return None

def chatbot():
    print("Gemini Chatbot: Hello! How can I assist you today? (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Gemini Chatbot: Goodbye!")
            break
        response = send_message(user_input)
        if response:
            print(f"Gemini Chatbot: {response}")
if __name__== "__main__":
    chatbot()