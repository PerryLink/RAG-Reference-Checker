# 使用指南

## 模型下载

RAG Reference Checker 需要使用 Sentence-Transformer 模型来计算语义相似度。由于网络原因,建议提前下载模型到本地。

### 推荐模型

1. **all-MiniLM-L6-v2** (推荐,轻量级)
   - 大小: ~80MB
   - 维度: 384
   - 适用: 英文为主的文本

2. **paraphrase-multilingual-MiniLM-L12-v2** (多语言支持)
   - 大小: ~420MB
   - 维度: 384
   - 适用: 中英文混合文本

### 下载方法

#### 方法 1: 使用 Python 脚本下载

```python
from sentence_transformers import SentenceTransformer

# 下载模型(会自动保存到缓存目录)
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# 查看模型缓存位置
import os
cache_dir = os.path.expanduser('~/.cache/torch/sentence_transformers')
print(f"模型缓存目录: {cache_dir}")
```

#### 方法 2: 手动下载

1. 访问 HuggingFace 模型页面:
   - https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

2. 点击 "Files and versions" 标签

3. 下载以下文件到本地目录(例如 `./models/all-MiniLM-L6-v2/`):
   - `config.json`
   - `pytorch_model.bin`
   - `tokenizer_config.json`
   - `vocab.txt`
   - `special_tokens_map.json`
   - `modules.json`
   - `sentence_bert_config.json`

#### 方法 3: 使用 Git LFS

```bash
# 安装 Git LFS
git lfs install

# 克隆模型仓库
git clone https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
```

## 使用示例

### 基本用法

```bash
# 使用本地模型
rag-reference-checker check \
  --input examples/sample_data.json \
  --model-path ./models/all-MiniLM-L6-v2

# 使用缓存的模型
rag-reference-checker check \
  --input examples/sample_data.json \
  --model-path sentence-transformers/all-MiniLM-L6-v2
```

### 调整相似度阈值

```bash
# 更严格的验证(阈值 0.7)
rag-reference-checker check \
  --input data.json \
  --model-path ./models/all-MiniLM-L6-v2 \
  --threshold 0.7

# 更宽松的验证(阈值 0.3)
rag-reference-checker check \
  --input data.json \
  --model-path ./models/all-MiniLM-L6-v2 \
  --threshold 0.3
```

### JSON 输出

```bash
# 输出 JSON 格式结果
rag-reference-checker check \
  --input data.json \
  --model-path ./models/all-MiniLM-L6-v2 \
  --json > result.json
```

## 输入格式

创建 JSON 文件,包含答案和参考文档:

```json
{
  "answer": "根据文档[1]，Python是一种解释型语言。此外[2]提到它支持多范式编程。",
  "references": [
    {
      "id": 1,
      "content": "Python is an interpreted, high-level programming language."
    },
    {
      "id": 2,
      "content": "Java is a compiled language with strong typing."
    }
  ]
}
```

## 输出格式

### 终端输出(默认)

```
┏━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 引用ID ┃ 状态          ┃ 相似度  ┃ 上下文                                              ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ [1]    │ ✓ valid       │ 0.87    │ 根据文档[1]，Python是一种解释型语言...              │
│ [2]    │ ✗ suspicious  │ 0.23    │ 此外[2]提到它支持多范式编程...                      │
└────────┴───────────────┴─────────┴──────────────────────────────────────────────────┘

总结: 2 个引用中有 1 个可疑
```

### JSON 输出

```json
{
  "total": 2,
  "valid": 1,
  "suspicious": 1,
  "details": [
    {
      "ref_id": 1,
      "status": "valid",
      "similarity": 0.87,
      "context": "根据文档[1]，Python是一种解释型语言"
    },
    {
      "ref_id": 2,
      "status": "suspicious",
      "similarity": 0.23,
      "context": "此外[2]提到它支持多范式编程",
      "reason": "低相似度"
    }
  ]
}
```

## 常见问题

### Q: 如何选择合适的相似度阈值?

A: 默认阈值 0.5 适用于大多数场景。如果发现:
- 太多误报(正确引用被标记为可疑): 降低阈值到 0.3-0.4
- 太多漏报(错误引用未被发现): 提高阈值到 0.6-0.7

### Q: 模型下载失败怎么办?

A:
1. 检查网络连接
2. 使用代理或镜像站点
3. 手动下载模型文件到本地
4. 使用已缓存的模型

### Q: 支持哪些语言?

A:
- `all-MiniLM-L6-v2`: 主要支持英文
- `paraphrase-multilingual-MiniLM-L12-v2`: 支持 50+ 种语言,包括中文

### Q: 如何提高验证准确度?

A:
1. 使用更大的模型(如 `all-mpnet-base-v2`)
2. 针对特定领域微调模型
3. 调整相似度阈值
4. 增加引用上下文窗口大小

## 性能优化

### 批量处理

如果需要验证大量文档,建议:
1. 复用同一个模型实例
2. 使用批量编码
3. 考虑使用 GPU 加速

### 模型选择

| 模型 | 大小 | 速度 | 准确度 | 适用场景 |
|------|------|------|--------|----------|
| all-MiniLM-L6-v2 | 80MB | 快 | 中 | 快速验证 |
| all-mpnet-base-v2 | 420MB | 中 | 高 | 高精度验证 |
| paraphrase-multilingual | 420MB | 中 | 中 | 多语言支持 |

## 集成示例

### Python 脚本

```python
from rag_reference_checker.core import ReferenceChecker

# 初始化验证器
checker = ReferenceChecker(
    model_path="./models/all-MiniLM-L6-v2",
    threshold=0.5
)

# 验证引用
answer = "根据文档[1]，Python是一种解释型语言。"
references = [
    {"id": 1, "content": "Python is an interpreted language."}
]

result = checker.verify_references(answer, references)
print(f"可疑引用数: {result['suspicious']}")
```

### CI/CD 集成

```yaml
# .github/workflows/check-references.yml
name: Check RAG References

on: [push, pull_request]

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install rag-reference-checker
          python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"
      - name: Check references
        run: |
          rag-reference-checker check \
            --input data.json \
            --model-path sentence-transformers/all-MiniLM-L6-v2 \
            --json > result.json
      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: reference-check-results
          path: result.json
```
