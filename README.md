# RAG Reference Checker

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)

A tool for verifying the authenticity of references in RAG (Retrieval-Augmented Generation) systems.

一个用于验证 RAG(检索增强生成)系统引用真实性的工具。

---

## Features | 核心特性

- **Automatic Citation Detection** - Extracts citation markers like `[1]`, `[2]` from AI-generated answers
- **Semantic Similarity Verification** - Uses Sentence-Transformers to compute semantic similarity between citations and reference documents
- **Configurable Threshold** - Adjustable similarity threshold to flag suspicious references
- **Rich CLI Output** - Beautiful terminal output with tables and color-coded results
- **JSON Export** - Export verification results in JSON format for further processing

---

- **自动引用检测** - 从 AI 生成的答案中提取 `[1]`、`[2]` 等引用标记
- **语义相似度验证** - 使用 Sentence-Transformers 计算引用与参考文档的语义相似度
- **可配置阈值** - 可调整相似度阈值以标记可疑引用
- **丰富的命令行输出** - 美观的终端输出,带表格和颜色编码结果
- **JSON 导出** - 以 JSON 格式导出验证结果供进一步处理

---

## Quick Start | 快速开始

### Installation | 安装

```bash
pip install rag-reference-checker
```

Or install from source | 或从源码安装:

```bash
git clone https://github.com/PerryLink/rag-reference-checker.git
cd rag-reference-checker
poetry install
```

### Download Model | 下载模型

First, download a Sentence-Transformer model. We recommend `all-MiniLM-L6-v2`:

首先需要下载 Sentence-Transformer 模型。推荐使用 `all-MiniLM-L6-v2`:

```bash
# Method 1: Download using Python | 方法 1: 使用 Python 下载
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"

# Method 2: Manual download | 方法 2: 手动下载
# Visit https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
# Download all files to a local directory, e.g., ./models/all-MiniLM-L6-v2/
# 访问 https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
# 下载所有文件到本地目录,例如 ./models/all-MiniLM-L6-v2/
```

### Basic Usage | 基本使用

Prepare input data in JSON format | 准备 JSON 格式的输入数据:

```json
{
  "answer": "According to document [1], Python is an interpreted language.",
  "references": [
    {
      "id": 1,
      "content": "Python is an interpreted, high-level programming language."
    }
  ]
}
```

Run verification | 运行验证:

```bash
rag-reference-checker check --input data.json --model-path ./models/all-MiniLM-L6-v2
```

---

## Usage Guide | 使用指南

### Command Options | 命令选项

```bash
# Basic verification | 基本验证
rag-reference-checker check --input data.json --model-path ./models/all-MiniLM-L6-v2

# Adjust similarity threshold | 调整相似度阈值
rag-reference-checker check --input data.json --model-path ./models/all-MiniLM-L6-v2 --threshold 0.7

# JSON output format | JSON 格式输出
rag-reference-checker check --input data.json --model-path ./models/all-MiniLM-L6-v2 --json

# Use different model | 使用不同模型
rag-reference-checker check --input data.json --model-path ./models/paraphrase-multilingual-MiniLM-L12-v2
```

### Parameters | 参数说明

- `--input, -i`: Path to JSON input file | JSON 输入文件路径
- `--model-path, -m`: Local model path or HuggingFace model name (required) | 本地模型路径或 HuggingFace 模型名称(必需)
- `--threshold, -t`: Similarity threshold (default: 0.5) | 相似度阈值(默认: 0.5)
- `--json`: Output results in JSON format | 以 JSON 格式输出结果

---

## How It Works | 工作原理

1. **Parse Citations** - Extract citation markers like `[1]`, `[2]` from the answer text
2. **Extract Context** - Extract surrounding context for each citation marker
3. **Compute Similarity** - Use Sentence-Transformers to calculate semantic similarity between context and reference documents
4. **Flag Suspicious** - Mark citations below the threshold as "suspicious"

---

1. **解析引用** - 从答案文本中提取 `[1]`、`[2]` 等引用标记
2. **提取上下文** - 为每个引用标记提取周围的上下文
3. **计算相似度** - 使用 Sentence-Transformers 计算上下文与参考文档的语义相似度
4. **标记可疑** - 将低于阈值的引用标记为"可疑"

---

## Project Structure | 项目结构

```
rag-reference-checker/
├── src/
│   └── rag_reference_checker/
│       ├── __init__.py
│       ├── cli.py           # Command-line interface | 命令行接口
│       ├── core.py          # Core verification logic | 核心验证逻辑
│       └── utils.py         # Utility functions | 工具函数
├── tests/
│   ├── test_cli.py
│   └── test_core.py
├── examples/
│   └── sample_data.json
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## Tech Stack | 技术栈

- **Python 3.8+**
- **sentence-transformers** - Semantic similarity computation | 语义相似度计算
- **numpy** - Numerical operations | 数值运算
- **click** - CLI framework | 命令行框架
- **rich** - Terminal formatting | 终端格式化
- **pytest** - Testing framework | 测试框架

---

## Development | 开发

```bash
# Install dependencies | 安装依赖
poetry install

# Run tests | 运行测试
pytest

# Code formatting | 代码格式化
black src/

# Linting | 代码检查
ruff check src/
```

---

## License | 许可证

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

本项目采用 Apache License 2.0 许可证 - 详见 [LICENSE](LICENSE) 文件。

Copyright 2026 Chance Dean <novelnexusai@outlook.com>

---

## Contributing | 贡献

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

欢迎贡献! 详见 [CONTRIBUTING.md](CONTRIBUTING.md)。
