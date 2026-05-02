import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from models.schemas import ResearchQuestion
from agent.searcher import search_question

q = ResearchQuestion(
    question="AI Agent 商业化",
    priority=5,
)

result = search_question(q)
print(result)