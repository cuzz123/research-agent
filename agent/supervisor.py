from langchain.chat_models import init_chat_model
from langchain_core.tools import tool
import os
import json
from dotenv import load_dotenv
from langchain.messages import HumanMessage
from models.schemas import ResearchPlan, ResearchQuestion

load_dotenv()

model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    openai_api_key=os.environ["DEEPSEEK_API_KEY"],
    openai_api_base="https://api.deepseek.com/v1",
    temperature=0,
)

def create_plan(topic: str) -> ResearchPlan:
    """根据调研主题，拆解成多个子问题"""
    prompt = f"""
    你是市场调研专家。请针对[{topic}]这个主题，拆解出3-5个需要调研的具体子问题。
    请严格按照以下JSON格式返回（不要加markdown代码块标记，只返回纯JSON）：
    {{
        "topic": "{topic}",
        "background": "该主题的背景说明",
        "questions": [
        {{"question": "具体的调研问题", "priority": 5}},
        {{"question": "另一个调研问题", "priority": 3}}
        ]
    }}
    """
    response = model.invoke([HumanMessage(content=prompt)])
    raw = response.content.strip()

    # 去掉可能的 markdown 代码块标记
    if raw.startswith(""):
        raw = raw.split("\n", 1)[1]
    if raw.endswith(""):
        raw = raw.rsplit("\n", 1)[0]

    # 如果缺少外层 {}，加上
    if not raw.startswith("{"):
        raw = "{" + raw
    if not raw.endswith("}"):
        raw = raw + "}"

    # print(f"=== 修复后的 JSON ===\n{raw}\n=== 结束 ===")
    data = json.loads(raw)
    return ResearchPlan(**data)

    # 去掉可能得markdown代码块标记
    # if raw.startswith(""):
    #     raw = raw.split("\n", 1)[1].rsplit("\n", 1)[0]
    #     if raw.endswith(""):
    #         raw = raw[:-3]
    #     print(f"=== LLM 原始返回 ===\n{raw}\n=== 结束 ===")
    #     data = json.loads(raw.strip())
    #     return ResearchPlan(**data)

    # structured_llm = model.with_structured_output(ResearchPlan)

    # result = structured_llm.invoke(
    #     f"你是市场调研专家，请针对[{topic}]这个主题，"
    #     f"拆解出3-5个需要调研的具体子问题。"
    #     f"包括主题背景说明，以及每个问题的优先级（1-5）。"
    # )
    # return result
