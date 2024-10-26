from cgitb import handler
from email import message
import os
import asyncio

from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler, AsyncChunkPrintHandler
from sparkai.core.messages import ChatMessage
try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError('Python environment for SPARK AI is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()

SPARK_API_URL = os.environ.get("SPARKAI_URL")
SPARK_APP_ID = os.environ.get("SPARKAI_APP_ID")
SPARK_API_KEY = os.environ.get("SPARKAI_API_KEY")
SPARK_API_SECRET = os.environ.get("SPARKAI_API_SECRET")
SPARK_LLM_DOMAIN = os.environ.get("SPARKAI_DOMAIN")

spark = ChatSparkLLM(
    spark_api_url=SPARK_API_URL,
    spark_app_id=SPARK_APP_ID,
    spark_api_key=SPARK_API_KEY,
    spark_api_secret=SPARK_API_SECRET,
    spark_llm_domain=SPARK_LLM_DOMAIN,
    streaming=False,
)

def explain(text: str):
    # 设置主题
    theme = f"你十分擅长文档阅读，现在你要阅读一份文档，并且给出详细的解释。"
    
    messages = [ChatMessage(
        role="system",
        content=theme
    ),
    ChatMessage(
        role="user",
        content=text
    )]

    handle = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handle])
    print(a.generations[0][0].text)

async def main():
    messages = [ChatMessage(
        role="user",
        content='你好呀'
    )]
    handler = AsyncChunkPrintHandler()
    a = spark.astream(messages, config={"callbacks": [handler]})
    async for response in a:
        print(response)

if __name__ == '__main__':
    asyncio.run(main())