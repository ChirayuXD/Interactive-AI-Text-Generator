from dotenv import load_dotenv
import os
import google.generativeai as genai

def configure_api():
    """Configure the Generative AI API."""
    load_dotenv()
    api_key = os.getenv('GCP_API_KEY')
    if not api_key:
        raise ValueError("GCP_API_KEY is not set in the environment variables")
    genai.configure(api_key=api_key)

def get_user_prompt():
    """Get a prompt from the user."""
    while True:
        prompt = input("Enter your prompt (or type 'exit' to quit): ")
        if prompt.strip().lower() == 'exit':
            return None
        if prompt.strip():
            return prompt
        print("Prompt cannot be empty. Please try again.")

def generate_response(model, prompt):
    """Generate and print the response from the model."""
    try:
        responses = model.generate_content(prompt, stream=True)
        for response in responses:
            print(response.text, end="")
            print("\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to run the prompt-response loop."""
    configure_api()
    model = genai.GenerativeModel("gemini-pro")

    while True:
        prompt = get_user_prompt()
        if prompt is None:
            print("Exiting the program.")
            break
        generate_response(model, prompt)
        continue_prompt = input("Would you like to continue (y/n)? ").strip().lower()
        if continue_prompt != 'y':
            break

if __name__ == "__main__":
    main()
