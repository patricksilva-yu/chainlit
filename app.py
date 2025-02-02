from openai import AsyncOpenAI
import chainlit as cl
from dotenv import load_dotenv
import os

load_dotenv()

client = AsyncOpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.getenv("API_KEY")
)

# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "deepseek-ai/DeepSeek-R1",
    "temperature": 0,
    # ... more settings
}

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
