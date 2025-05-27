from openai_client import ask_openai

if __name__ == "__main__":
    prompt = "Say hello in a friendly way."
    answer = ask_openai(prompt)
    print("OpenAI response:", answer)
