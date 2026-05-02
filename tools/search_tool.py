from langchain_core.tools import tool
# from langchain_tavily import TavilySearch
from tavily import TavilyClient
import os

# 模拟搜索结果库
# MOCK_DB = {
#         "AI Agent 商业化": [
#             "2025年全球AI Agent市场规模预计达420亿美元，年复合增长率44%",
#             "企业级AI Agent平均部署周期3-6个月，ROI周期约8-12个月",
#             "客服、代码生成、营销文案是当前三大付费场景",
#         ],
#         "AI Agent 技术栈": [
#             "LangGraph/LangChain占据Agent框架市场份额超60%",
#             "MCP协议成为行业标准，Anthropic/OpenAI/Google均已支持",
#             "开源方案（LangChain + FastMCP）可降低60%以上开发成本",
#         ],
#         "AI Agent 竞争格局": [
#             "微软Copilot生态、字节Coze、谷歌Vertex AI Agent占据头部",
#             "垂直行业Agent（医疗、法律、金融）仍有大量空白市场",
#             "2025年Q1 AI Agent创业融资总额超80亿美元",
#         ],
#     }

@tool
def search_topic(keyword: str) -> str:
    """
    搜索指定关键词的相关信息。

    Args:
        keyword: 搜索关键词

    Returns:
        搜索到的相关条目
    """
    # results = []
    # for key, items in MOCK_DB.items():
    #     if keyword in key or any(keyword in item for item in items):
    #         results.extend(items)
    
    # # 模糊匹配：关键词包含“商业化”也匹配“AI Agent 商业化”
    # for key, items in MOCK_DB.items():
    #     for item in items:
    #         if any(kw in item for kw in keyword.split()):
    #             results.extend(items)
    #             break

    # if not results:
    #     results = [f"没有找到与【{keyword}】直接相关的结果"]

    # return "\n".join(set(results))
    client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    results = client.search(query=keyword, max_results=5)

    if not results.get("results"):
        return f"未找到与【{keyword}】相关的结果"

    lines = []
    for r in results["results"]:
        lines.append(f"标题：{r.get('title', '无标题')}")
        lines.append(f"摘要：{r.get('content', '无内容')}")
        lines.append(f"链接：{r.get('url', '')}")
        lines.append("---")

    return "\n".join(lines)