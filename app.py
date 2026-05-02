from fastapi import FastAPI
from pydantic import BaseModel
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from agent.supervisor import create_plan
from agent.searcher import search_question
from agent.analyzer import analyze_search_result
from agent.writer import write_report

app = FastAPI(title="调研助手 API")

class ResearchRequest(BaseModel):
    topic: str

class ResearchResponse(BaseModel):
    report: str

@app.post("/research")
async def do_research(req: ResearchRequest) -> ResearchResponse:
    """接收调研主题，返回 Markdown 报告"""
    # 1. 拆解问题
    plan = create_plan(req.topic)

    # 2. 搜索 + 分析
    findings = []
    for q in plan.questions:
        raw = search_question(q)
        finding = analyze_search_result(q.question, raw)
        findings.append(finding)

    # 3. 生成报告
    report = write_report(plan.topic, findings)
    return ResearchResponse(report=report)

@app.get("/")
def root():
    return {"message": "调研助手API已启动", "使用方式": "POST /research Body: {\"topic\": \"调研主题\"}"}

