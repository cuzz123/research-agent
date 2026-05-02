from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    openai_api_key=os.environ["DEEPSEEK_API_KEY"],
    openai_api_base=os.environ["DEEPSEEK_BASE_URL"],
)

def write_report(topic: str, findings: list) -> str:
    """根据调研发现，生成结构化Markdown报告"""
    findings_text = ""
    for f in findings:
        findings_text += f"""
        {f.question}
        摘要：{f.summary}
        详细分析：{f.details}
        """

    prompt = f"""你是一个专业调研报告撰写员。请根据以下调研发现，撰写一份结构化的Markdown调研报告。
    调研主题：{topic}
    调研发现：
    {findings_text}

    请输出一份完整的Markdown报告，包括：
    1. 标题
    2. 摘要
    3. 分章节分析（每个调研发现一个章节）
    4. 结论与建议
    """
    response = model.invoke([HumanMessage(content=prompt)])
    return response.content

    