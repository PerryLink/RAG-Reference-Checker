# Contributing to RAG Reference Checker

Thank you for your interest in contributing to RAG Reference Checker!

感谢您对 RAG Reference Checker 项目的关注!

---

## Project Status | 项目状态

This is currently a **personal project** maintained by Chance Dean. While contributions are welcome, please note that:

这是一个由 Chance Dean 个人维护的项目。虽然欢迎贡献,但请注意:

- The project is maintained on a best-effort basis
- Response times may vary
- Major architectural decisions are made by the project owner

---

- 项目基于尽力而为的原则维护
- 响应时间可能有所不同
- 重大架构决策由项目所有者做出

---

## How to Report Issues | 如何报告问题

If you encounter a bug or have a feature request:

如果您遇到错误或有功能请求:

1. **Check existing issues** - Search the [issue tracker](https://github.com/PerryLink/rag-reference-checker/issues) to see if the issue has already been reported
2. **Create a new issue** - If not found, create a new issue with:
   - A clear, descriptive title
   - Detailed description of the problem or feature
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (Python version, OS, etc.)

---

1. **检查现有问题** - 在 [issue tracker](https://github.com/PerryLink/rag-reference-checker/issues) 中搜索是否已有相关问题
2. **创建新问题** - 如果没有找到,创建新问题并包含:
   - 清晰、描述性的标题
   - 问题或功能的详细描述
   - 重现步骤(针对错误)
   - 预期行为与实际行为
   - 您的环境(Python 版本、操作系统等)

---

## Development Setup | 开发环境搭建

### Prerequisites | 前置要求

- Python 3.8 or higher
- Poetry (for dependency management)
- Git

---

- Python 3.8 或更高版本
- Poetry(用于依赖管理)
- Git

### Setup Steps | 搭建步骤

1. **Fork and clone the repository** | **Fork 并克隆仓库**

```bash
git clone https://github.com/PerryLink/rag-reference-checker.git
cd rag-reference-checker
```

2. **Install dependencies** | **安装依赖**

```bash
poetry install
```

3. **Download a test model** | **下载测试模型**

```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"
```

4. **Run tests to verify setup** | **运行测试以验证设置**

```bash
pytest
```

---

## Code Standards | 代码规范

This project follows **PEP 8** style guidelines. Please ensure your code adheres to these standards:

本项目遵循 **PEP 8** 风格指南。请确保您的代码符合这些标准:

### Formatting | 格式化

```bash
# Format code with Black | 使用 Black 格式化代码
black src/ tests/

# Check code with Ruff | 使用 Ruff 检查代码
ruff check src/ tests/
```

### Key Guidelines | 关键指南

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (Black default)
- Use descriptive variable and function names
- Add docstrings for public functions and classes
- Write type hints where appropriate

---

- 使用 4 个空格缩进(不使用制表符)
- 最大行长度: 88 字符(Black 默认值)
- 使用描述性的变量和函数名
- 为公共函数和类添加文档字符串
- 在适当的地方编写类型提示

---

## Pull Request Process | 提交 Pull Request 流程

1. **Create a feature branch** | **创建功能分支**

```bash
git checkout -b feature/your-feature-name
```

2. **Make your changes** | **进行更改**
   - Write clean, well-documented code
   - Add tests for new functionality
   - Ensure all tests pass

---

   - 编写清晰、文档完善的代码
   - 为新功能添加测试
   - 确保所有测试通过

3. **Run quality checks** | **运行质量检查**

```bash
# Run tests | 运行测试
pytest

# Format code | 格式化代码
black src/ tests/

# Check linting | 检查代码规范
ruff check src/ tests/
```

4. **Commit your changes** | **提交更改**

```bash
git add .
git commit -m "feat: add your feature description"
```

Follow conventional commit format:
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `test:` - Test additions or changes
- `refactor:` - Code refactoring

---

遵循约定式提交格式:
- `feat:` - 新功能
- `fix:` - 错误修复
- `docs:` - 文档更改
- `test:` - 测试添加或更改
- `refactor:` - 代码重构

5. **Push to your fork** | **推送到您的 fork**

```bash
git push origin feature/your-feature-name
```

6. **Create a Pull Request** | **创建 Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your feature branch
   - Provide a clear description of your changes
   - Reference any related issues

---

   - 访问 GitHub 上的原始仓库
   - 点击 "New Pull Request"
   - 选择您的功能分支
   - 提供清晰的更改描述
   - 引用任何相关问题

---

## Testing | 测试

All new features should include appropriate tests:

所有新功能都应包含适当的测试:

```bash
# Run all tests | 运行所有测试
pytest

# Run with coverage | 运行并显示覆盖率
pytest --cov=src/rag_reference_checker

# Run specific test file | 运行特定测试文件
pytest tests/test_core.py
```

---

## Questions? | 有问题?

If you have questions about contributing, feel free to:

如果您对贡献有疑问,请随时:

- Open an issue for discussion
- Contact the maintainer at novelnexusai@outlook.com

---

- 开启一个问题进行讨论
- 通过 novelnexusai@outlook.com 联系维护者

---

## License | 许可证

By contributing to this project, you agree that your contributions will be licensed under the Apache License 2.0.

通过为本项目做出贡献,您同意您的贡献将根据 Apache License 2.0 许可。

---

Thank you for contributing! 感谢您的贡献!
