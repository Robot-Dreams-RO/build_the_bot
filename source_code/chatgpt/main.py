import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    """Generate a response using GPT-3.5."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with the appropriate GPT-3.5 chat model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,  # Limit the response length
            n=1,            # Number of responses to generate
            stop="\n"       # Stop generating response after encountering a newline character
        )

        generated_text = response.choices[0].message['content'].strip()
        return generated_text

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def chatbot():
    """Chatbot that uses GPT-3.5 to generate responses."""
    print("Welcome to the GPT-3.5 Chatbot! (type 'quit' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        response = generate_response(user_input)
        if response:
            print(f"AI: {response}")
        else:
            print("Error generating response. Please try again.")

if __name__ == "__main__":
    chatbot()