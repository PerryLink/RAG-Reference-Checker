"""核心逻辑测试"""
import pytest
from rag_reference_checker.core import ReferenceChecker
from rag_reference_checker.utils import extract_citations, extract_context


def test_extract_citations():
    text = "这是测试[1]，还有[2]和[3]"
    citations = extract_citations(text)
    assert len(citations) == 3
    assert citations[0][0] == 1
    assert citations[1][0] == 2
    assert citations[2][0] == 3


def test_extract_context():
    text = "这是一段很长的文本，中间有引用标记"
    context = extract_context(text, 10, window=5)
    assert len(context) <= 10


def test_reference_checker():
    # 注意: 此测试需要预先下载模型
    # 在实际测试中,应该使用 mock 或提供测试模型路径
    try:
        checker = ReferenceChecker(
            model_path="sentence-transformers/all-MiniLM-L6-v2",
            threshold=0.5
        )
        answer = "Python is a programming language[1]"
        references = [
            {"id": 1, "content": "Python is an interpreted programming language"}
        ]
        result = checker.verify_references(answer, references)
        assert result["total"] == 1
        assert result["details"][0]["status"] == "valid"
    except ValueError:
        # 如果模型不可用,跳过测试
        pass
