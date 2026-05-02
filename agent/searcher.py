from tools.search_tool import search_topic

def search_question(question) -> str:
    """对单个调研问题进行搜索
    Args:
        question: ResearchQuestion对象，包含question和priority字段
    Returns:
        搜索结果的原始文本
    """
    # question.question 就是"2025年企业客户对AI Agent的核心付费意愿..."
    raw = search_topic.invoke({"keyword": question.question})
    return raw