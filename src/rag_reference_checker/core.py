"""核心验证逻辑"""
from typing import List, Dict, Any, Optional
import numpy as np
from sentence_transformers import SentenceTransformer
from .utils import extract_citations, extract_context


class ReferenceChecker:
    """引用验证器"""

    def __init__(self, model_path: Optional[str] = None, threshold: float = 0.5):
        """初始化验证器

        Args:
            model_path: 本地模型路径或 HuggingFace 模型名称
                       如果为 None,将使用默认的轻量级模型(需要网络下载)
            threshold: 相似度阈值
        """
        if model_path is None:
            raise ValueError(
                "请指定模型路径。您可以:\n"
                "1. 下载模型到本地,然后使用 --model-path 指定路径\n"
                "2. 使用 HuggingFace 模型名称(需要网络连接)\n"
                "推荐模型: sentence-transformers/all-MiniLM-L6-v2\n"
                "下载地址: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2"
            )
        self.model = SentenceTransformer(model_path)
        self.threshold = threshold

    def compute_similarity(self, text1: str, text2: str) -> float:
        """计算两段文本的余弦相似度

        Args:
            text1: 第一段文本
            text2: 第二段文本

        Returns:
            相似度分数 (0-1)
        """
        embeddings = self.model.encode([text1, text2])
        similarity = np.dot(embeddings[0], embeddings[1]) / (
            np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1])
        )
        return float(similarity)

    def verify_references(self, answer: str, references: List[Dict[str, Any]]) -> Dict[str, Any]:
        """验证答案中的引用

        Args:
            answer: 包含引用标记的答案文本
            references: 参考文档列表，每个元素包含 id 和 content

        Returns:
            验证结果字典
        """
        citations = extract_citations(answer)
        ref_dict = {ref["id"]: ref["content"] for ref in references}

        results = []
        for ref_id, start_pos, end_pos in citations:
            if ref_id not in ref_dict:
                results.append({
                    "ref_id": ref_id,
                    "status": "missing",
                    "similarity": 0.0,
                    "context": extract_context(answer, start_pos),
                    "reason": "引用的文档不存在"
                })
                continue

            context = extract_context(answer, start_pos)
            ref_content = ref_dict[ref_id]
            similarity = self.compute_similarity(context, ref_content)

            status = "valid" if similarity >= self.threshold else "suspicious"
            result = {
                "ref_id": ref_id,
                "status": status,
                "similarity": round(similarity, 2),
                "context": context
            }

            if status == "suspicious":
                result["reason"] = "低相似度"

            results.append(result)

        valid_count = sum(1 for r in results if r["status"] == "valid")
        suspicious_count = sum(1 for r in results if r["status"] == "suspicious")

        return {
            "total": len(results),
            "valid": valid_count,
            "suspicious": suspicious_count,
            "details": results
        }
