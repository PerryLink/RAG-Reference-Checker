<div align="center">

# RAG-Reference-Checker

**A CLI tool that checks whether the citations in a RAG answer really match their reference documents.**

*Ported into [dsh-library](https://github.com/PerryLink/dsh-library) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

RAG systems attach citations such as `[1]` or `[2]` to generated answers. RAG-Reference-Checker extracts those markers, looks up each referenced document, and uses Sentence-Transformers to compute the semantic similarity between the citation's surrounding context and the referenced content. Citations below a configurable threshold are flagged as suspicious.

## Features

- Extracts citation markers (`[1]`, `[2]`, …) from answers
- Computes semantic similarity with Sentence-Transformers
- Configurable similarity threshold
- Color-coded terminal table or JSON output
- Marks references whose document is missing

## Quick start

Requires Python 3.8+ and [Poetry](https://python-poetry.org/).

```bash
git clone https://github.com/PerryLink/RAG-Reference-Checker.git
cd RAG-Reference-Checker
poetry install
```

Download a Sentence-Transformer model (e.g. `all-MiniLM-L6-v2`):

```bash
python download_model.py sentence-transformers/all-MiniLM-L6-v2 ./models/all-MiniLM-L6-v2
```

## Usage

Prepare a JSON input file:

```json
{
  "answer": "According to document [1], Python is an interpreted language.",
  "references": [
    { "id": 1, "content": "Python is an interpreted, high-level programming language." }
  ]
}
```

Run the check:

```bash
rag-reference-checker check --input data.json --model-path ./models/all-MiniLM-L6-v2
```

| Option | Default | Description |
|--------|---------|-------------|
| `--input`, `-i` | — | Path to the JSON input file |
| `--model-path`, `-m` | — | Local model path or HuggingFace model name (required) |
| `--threshold`, `-t` | `0.5` | Similarity threshold |
| `--json` | off | Print the result as JSON |

```bash
# Raise the threshold and print JSON
rag-reference-checker check --input data.json --model-path ./models/all-MiniLM-L6-v2 --threshold 0.7 --json
```

## Development

```bash
poetry run pytest -v
poetry run black src/
poetry run ruff check src/
```

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
