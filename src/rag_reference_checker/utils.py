"""工具函数"""
import re
from typing import List, Tuple


def extract_citations(text: str) -> List[Tuple[int, int, int]]:
    """提取文本中的引用标记及其位置

    Args:
        text: 包含引用标记的文本

    Returns:
        List of (ref_id, start_pos, end_pos)
    """
    pattern = r'\[(\d+)\]'
    matches = []
    for match in re.finditer(pattern, text):
        ref_id = int(match.group(1))
        matches.append((ref_id, match.start(), match.end()))
    return matches


def extract_context(text: str, position: int, window: int = 50) -> str:
    """提取引用标记周围的上下文

    Args:
        text: 完整文本
        position: 引用标记位置
        window: 上下文窗口大小（字符数）

    Returns:
        上下文文本
    """
    start = max(0, position - window)
    end = min(len(text), position + window)
    return text[start:end].strip()
