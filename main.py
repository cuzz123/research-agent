import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from agent.supervisor import create_plan
from agent.searcher import search_question
from agent.analyzer import analyze_search_result
from agent.writer import write_report

# 1. 拆解问题
plan = create_plan("AI Agent 赛道创业")
print(f"调研主题：{plan.topic}")
# print(f"背景：{plan.background}\n")
# print("子问题：")
# for q in plan.questions:
#     print(f" [优先级 {q.priority}] {q.question}")

# 2. 搜索 + 分析每个子问题
findings = []
for q in plan.questions:
    print(f"   调研：{q.question[:30]}...")
    raw = search_question(q)
    finding = analyze_search_result(q.question, raw)
    findings.append(finding)

# 3. 生成报告
print(f"\n 生成报告...")
report = write_report(plan.topic, findings)

print("\n" + "=" * 50)
print(report)