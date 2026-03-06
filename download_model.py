#!/usr/bin/env python3
"""
模型下载脚本

使用方法:
    python download_model.py [模型名称] [保存路径]

示例:
    python download_model.py sentence-transformers/all-MiniLM-L6-v2 ./models/all-MiniLM-L6-v2
"""

import sys
import os
from sentence_transformers import SentenceTransformer


def download_model(model_name: str, save_path: str = None):
    """下载 Sentence-Transformer 模型

    Args:
        model_name: HuggingFace 模型名称
        save_path: 保存路径(可选)
    """
    print(f"正在下载模型: {model_name}")
    print("这可能需要几分钟时间,请耐心等待...")

    try:
        # 下载模型
        model = SentenceTransformer(model_name)

        # 如果指定了保存路径,则保存模型
        if save_path:
            os.makedirs(save_path, exist_ok=True)
            model.save(save_path)
            print(f"\n✓ 模型已保存到: {save_path}")
        else:
            # 显示缓存位置
            cache_dir = os.path.expanduser('~/.cache/torch/sentence_transformers')
            print(f"\n✓ 模型已下载到缓存目录: {cache_dir}")

        print("\n模型信息:")
        print(f"  - 模型名称: {model_name}")
        print(f"  - 向量维度: {model.get_sentence_embedding_dimension()}")
        print(f"  - 最大序列长度: {model.max_seq_length}")

        # 测试模型
        print("\n测试模型...")
        test_text = "This is a test sentence."
        embedding = model.encode(test_text)
        print(f"✓ 模型测试成功! 向量维度: {len(embedding)}")

    except Exception as e:
        print(f"\n✗ 下载失败: {str(e)}")
        print("\n可能的解决方案:")
        print("1. 检查网络连接")
        print("2. 使用代理或 VPN")
        print("3. 手动从 HuggingFace 下载模型文件")
        print(f"   下载地址: https://huggingface.co/{model_name}")
        sys.exit(1)


def main():
    # 默认模型
    default_model = "sentence-transformers/all-MiniLM-L6-v2"

    if len(sys.argv) < 2:
        print("使用默认模型:", default_model)
        model_name = default_model
        save_path = None
    elif len(sys.argv) == 2:
        model_name = sys.argv[1]
        save_path = None
    else:
        model_name = sys.argv[1]
        save_path = sys.argv[2]

    download_model(model_name, save_path)


if __name__ == "__main__":
    main()
