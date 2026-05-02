from pydantic import BaseModel, Field
from typing import List, Optional

class ResearchQuestion(BaseModel):
    """调研子问题"""
    question: str = Field(description="具体的调研问题")
    priority: int = Field(description="优先级，1-5")

class ResearchPlan(BaseModel):
    """调研计划"""
    topic: str = Field(description="调研主题")
    questions: List[ResearchQuestion] = Field(description="拆解后的子问题清单")
    background: str = Field(description="主题背景说明")

class Finding(BaseModel):
    """调研发现"""
    question: str = Field(description="对应的调研问题")
    summary: str = Field(description="调研结论摘要")
    details: str = Field(description="详细内容")
    sources: List[str] = Field(default_factory=list, description="信息来源")

class ResearchReport(BaseModel):
    """最终调研报告"""
    title: str
    summary: str
    findings: List[Finding]
    conclusion: str