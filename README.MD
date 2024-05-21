# Interactive AI Text Generator

This project is an interactive text generation tool that leverages the power of Google's Generative AI model, "gemini-pro". Users can input prompts, and the AI generates and streams responses in real-time. The interaction continues until the user decides to exit.

## Features

- **Real-time Streaming Responses**: Get immediate responses from the AI model.
- **Interactive User Interface**: Continuously provide prompts and receive responses.
- **Error Handling**: Handles errors gracefully to ensure smooth user experience.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- An API key for Google's Generative AI
- Required Python packages: `python-dotenv` and `google-generativeai`

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/interactive-ai-text-generator.git
   cd interactive-ai-text-generator
   ```

2. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add your Google Cloud API key:
   ```sh
   touch .env
   echo "GCP_API_KEY=your_google_cloud_api_key_here" > .env
   ```

3. **Install Required Packages**:
   ```sh
   pip install -r requirements.txt
   ```

### Usage

Run the script to start the interactive prompt-response loop:
```sh
python main.py
```

1. **Enter your prompt**: Type a prompt and press Enter.
2. **Receive response**: The AI will generate and stream a response.
3. **Continue or Exit**: Type 'y' to continue with another prompt or 'n' to exit the program. You can also type 'exit' at any prompt to quit.

### Example

```sh
$ python main.py
Enter your prompt (or type 'exit' to quit): Hello, AI!
AI Response: Hello! How can I assist you today?

Would you like to continue (y/n)? y
Enter your prompt (or type 'exit' to quit): Tell me a joke.
AI Response: Why don't scientists trust atoms? Because they make up everything!

Would you like to continue (y/n)? n
Exiting the program.
```



## Acknowledgements

- [Google Generative AI](https://cloud.google.com/generative-ai)
- [Python Dotenv](https://github.com/theskumar/python-dotenv)

---
