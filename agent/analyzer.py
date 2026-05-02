from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
import json, os
from dotenv import load_dotenv
from models.schemas import Finding

load_dotenv()

model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    openai_api_key=os.environ["DEEPSEEK_API_KEY"],
    openai_api_base=os.environ["DEEPSEEK_BASE_URL"],
    temperature=0,
)

def analyze_search_result(question_text: str, search_result: str) -> Finding:
    """从搜索结果中提取关键信息，返回结构化的Finding"""

    prompt = f"""你是一个调研分析员。请根据以下搜索结果，提炼出关键信息。
    调研问题： {question_text}
    搜索结果： {search_result}
    请严格按照以下JSON格式返回(只返回纯JSON)：
    {{"question": "{question_text}", "summary": "一句话总结", "details": "详细分析", "source": ["来源1", "来源2"]}}
    """
    
    response = model.invoke([HumanMessage(content=prompt)])
    raw = response.content.strip()

    # 清理可能得markdown标记
    # if raw.startswith(""):
    #     raw = raw.split("\n", 1)[1]
    # if raw.endswith(""):
    #     raw = raw.rsplit("\n", 1)[0]

    data = json.loads(raw)
    return Finding(**data)