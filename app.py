from openai import AsyncOpenAI
import chainlit as cl
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = AsyncOpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.getenv("API_KEY")
)

# Instrument the OpenAI client
cl.instrument_openai()

# Define model settings
settings = {
    "model": "deepseek-ai/DeepSeek-R1",
    "temperature": 0,
    # ... more settings
}

# Define the message handler
@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "deepseek-ai/DeepSeek-R1",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()

# Entry point for the Chainlit app
if __name__ == "__main__":
    cl.run(
        host="0.0.0.0",  # Bind to all interfaces
        port=int(os.environ.get("PORT", 8000))  # Use Render's $PORT or default to 8000
    )