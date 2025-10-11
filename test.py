import os
from openai import OpenAI

# Option 1: Use environment variable (recommended)
api_key = os.getenv("OPENAI_API_KEY")

# Option 2: Directly paste your key (for quick testing only)
# api_key = "sk-your-api-key-here"

client = OpenAI(api_key=api_key)

def test_api():
    try:
        # List available models
        models = client.models.list()
        print("✅ API key is valid!")
        print("Available models (showing first 5):")
        for m in models.data[:5]:
            print("-", m.id)
        
        # Optional: Test a quick response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "Say hello in a friendly way."}
            ]
        )
        print("\nTest response from model:")
        print(response.choices[0].message.content)

    except Exception as e:
        print("❌ API key validation failed!")
        print("Error:", e)

if __name__ == "__main__":
    test_api()