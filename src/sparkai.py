import os

from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
try:
    from dotenv import load_dotenv
except ImportError:
    raise RuntimeError('Python environment for SPARK AI is not completely set up: required package "python-dotenv" is missing.') from None

load_dotenv()

if __name__ == '__main__':
    from sparkai.core.callbacks import StdOutCallbackHandler
    spark = ChatSparkLLM(
        spark_api_url=os.environ["SPARKAI_URL"],
        spark_app_id=os.environ["SPARKAI_APP_ID"],
        spark_api_key=os.environ["SPARKAI_API_KEY"],
        spark_api_secret=os.environ["SPARKAI_API_SECRET"],
        spark_llm_domain=os.environ["SPARKAI_DOMAIN"],
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content='你好呀'
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    print(a)
    print(a.generations[0][0].text)
    print(a.llm_output)