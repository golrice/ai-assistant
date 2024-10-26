from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler, AsyncChunkPrintHandler
from sparkai.core.messages import ChatMessage
import os
from sparkai.core.utils.function_calling import convert_to_openai_tool, convert_to_openai_function
import json
from dotenv import load_dotenv

load_dotenv()

SPARK_API_URL = os.environ.get("SPARKAI_URL")
SPARK_APP_ID = os.environ.get("SPARKAI_APP_ID")
SPARK_API_KEY = os.environ.get("SPARKAI_API_KEY")
SPARK_API_SECRET = os.environ.get("SPARKAI_API_SECRET")
SPARK_LLM_DOMAIN = os.environ.get("SPARKAI_DOMAIN")

def multiply(a,b :int) -> int:
    """你是一个乘法计算器，可以帮我计算两个数的乘积，例如：计算1乘1等于几或计算1*1等于几
    Args:
        a: 输入a
        b: 输入b
    Return:
         返回 a*b 结果
    """
    print("hello success")
    return a*b

def test_function_call():
    from sparkai.core.callbacks import StdOutCallbackHandler
    messages = [{'role': 'user',
                 'content': "帮我算下 12乘以12"}]
    spark = ChatSparkLLM(
        spark_api_url=SPARK_API_URL,
        spark_app_id=SPARK_APP_ID,
        spark_api_key=SPARK_API_KEY,
        spark_api_secret=SPARK_API_SECRET,
        spark_llm_domain=SPARK_LLM_DOMAIN,
        streaming=False,

    )
    function_definition =[convert_to_openai_function(multiply)]
    print(json.dumps(convert_to_openai_tool(multiply),ensure_ascii=False))
    messages = [ChatMessage(
        role="user",
        content=messages[0]['content']

    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler],function_definition=function_definition)
    print(a)
    print(a.generations[0][0].text) 
    print(a.llm_output)

if __name__ == "__main__":
    test_function_call()