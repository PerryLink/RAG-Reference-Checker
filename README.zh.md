<div align="center">

# RAG-Reference-Checker

**用于校验 RAG 生成答案中的引用是否与参考文档真实匹配的命令行工具。**

*已移植到 [dsh-library](https://github.com/PerryLink/dsh-library) —— PerryLink DSH 插件家族的一员。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

RAG 系统会在生成的答案中附加 `[1]`、`[2]` 等引用标记。RAG-Reference-Checker 会提取这些标记，查找每篇被引用的文档，并使用 Sentence-Transformers 计算引用上下文与参考内容之间的语义相似度。低于可配置阈值的引用会被标记为「可疑」。

## 功能特性

- 从答案中提取 `[1]`、`[2]` 等引用标记
- 使用 Sentence-Transformers 计算语义相似度
- 相似度阈值可配置
- 输出彩色终端表格或 JSON
- 标记引用文档缺失的情况

## 快速开始

需要 Python 3.8+ 与 [Poetry](https://python-poetry.org/)。

```bash
git clone https://github.com/PerryLink/RAG-Reference-Checker.git
cd RAG-Reference-Checker
poetry install
```

下载一个 Sentence-Transformer 模型（如 `all-MiniLM-L6-v2`）：

```bash
python download_model.py sentence-transformers/all-MiniLM-L6-v2 ./models/all-MiniLM-L6-v2
```

## 使用方法

准备一个 JSON 输入文件：

```json
{
  "answer": "According to document [1], Python is an interpreted language.",
  "references": [
    { "id": 1, "content": "Python is an interpreted, high-level programming language." }
  ]
}
```

运行校验：

```bash
rag-reference-checker check --input data.json --model-path ./models/all-MiniLM-L6-v2
```

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--input`, `-i` | — | JSON 输入文件路径 |
| `--model-path`, `-m` | — | 本地模型路径或 HuggingFace 模型名称（必需） |
| `--threshold`, `-t` | `0.5` | 相似度阈值 |
| `--json` | 关 | 以 JSON 格式输出结果 |

```bash
# 提高阈值并以 JSON 输出
rag-reference-checker check --input data.json --model-path ./models/all-MiniLM-L6-v2 --threshold 0.7 --json
```

## 开发

```bash
poetry run pytest -v
poetry run black src/
poetry run ruff check src/
```

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
