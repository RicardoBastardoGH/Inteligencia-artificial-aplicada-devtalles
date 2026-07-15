
from openai import OpenAI, AuthenticationError, RateLimitError, APIConnectionError
from dotenv import load_dotenv
import os

load_dotenv()


def call_ai(question):
    """
    Calls the OpenAI API with the provided question and returns the response.
    """
    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL"),
            messages=[
                {
                    "role": "user", 
                    "content": question
                }
            ],
            max_tokens=500,
            temperature=0.7 # 0=determinista, 1=creativo, 2=muy creativo / caotico
        )
        return response.choices[0].message.content
    except AuthenticationError:
        print ("Authentication failed. Please check your API key.")
        raise SystemExit(1)
    except RateLimitError:
        print ("Rate limit exceeded. Please try again later.")
        raise 
    except APIConnectionError:
        print ("Server connection error. Please check your internet connection and try again.")
        raise 
    except Exception as e:
        print(f"An error occurred while calling the AI: {type(e).__name__}: {e}")
        raise 
            
if __name__ == "__main__":
    question = "What is the capital of France?"
    response = call_ai(question)
    print(f"Answer: {response}")

