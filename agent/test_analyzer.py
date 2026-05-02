import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from models.schemas import Finding
from agent.searcher import search_question
from agent.analyzer import analyze_search_result
from models.schemas import ResearchQuestion

q = ResearchQuestion(question="AI Agent 商业化", priority=5)
raw = search_question(q)
finding = analyze_search_result(q.question, raw)
print(f"问题：{finding.question}")
print(f"总结：{finding.summary}")
print(f"详情：{finding.details}")