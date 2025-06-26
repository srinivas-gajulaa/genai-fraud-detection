from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the API key from the actual env variable name
openai_api_key = os.getenv("OPENAI_API_KEY")

# Debug: show whether the key was loaded
print("🔑 OPENAI_API_KEY loaded:", openai_api_key[:8] + "..." if openai_api_key else "❌ NOT FOUND")

# Initialize the LLM
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.3,
    openai_api_key=openai_api_key
)

# Prompt template
template = """
You are a compliance analyst assistant. Based on the features below, write a one-line fraud risk summary:

- Amount: {amount}
- Location Changed: {location_change}
- Velocity: {velocity}
- Time of Day: {time_of_day}
- ML Score: {score}

Summary:
"""

prompt = PromptTemplate.from_template(template)

# Safe wrapper to generate summary
def generate_summary(txn: dict) -> str:
    try:
        return llm.predict(prompt.format(**txn))
    except Exception as e:
        print("🔥 GPT Error:", e)
        return "Summary generation failed"
