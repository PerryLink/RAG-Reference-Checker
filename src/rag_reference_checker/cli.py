"""CLI 命令行接口"""
import json
import click
from rich.console import Console
from rich.table import Table
from .core import ReferenceChecker


console = Console()


@click.group()
def cli():
    """RAG Reference Checker - 验证 RAG 系统引用真实性"""
    pass


@cli.command()
@click.option("--input", "-i", type=click.Path(exists=True), help="JSON 输入文件路径")
@click.option("--answer", "-a", help="答案文本")
@click.option("--threshold", "-t", default=0.5, help="相似度阈值 (默认: 0.5)")
@click.option("--json", "output_json", is_flag=True, help="以 JSON 格式输出")
@click.option("--model-path", "-m", required=True, help="本地模型路径或 HuggingFace 模型名称")
def check(input, answer, threshold, output_json, model_path):
    """检查引用的真实性"""

    # 读取输入
    if input:
        with open(input, "r", encoding="utf-8") as f:
            data = json.load(f)
        answer_text = data["answer"]
        references = data["references"]
    elif answer:
        console.print("[red]错误: 使用 --answer 时需要通过 --input 提供完整数据[/red]")
        return
    else:
        console.print("[red]错误: 必须提供 --input 参数[/red]")
        return

    # 执行验证
    try:
        checker = ReferenceChecker(model_path=model_path, threshold=threshold)
        result = checker.verify_references(answer_text, references)
    except Exception as e:
        console.print(f"[red]错误: {str(e)}[/red]")
        return

    # 输出结果
    if output_json:
        console.print_json(data=result)
    else:
        table = Table(title="引用验证结果")
        table.add_column("引用ID", style="cyan")
        table.add_column("状态", style="magenta")
        table.add_column("相似度", style="green")
        table.add_column("上下文", style="yellow")

        for detail in result["details"]:
            status_icon = "✓" if detail["status"] == "valid" else "✗"
            status_color = "green" if detail["status"] == "valid" else "red"
            status_text = f"[{status_color}]{status_icon} {detail['status']}[/{status_color}]"

            table.add_row(
                f"[{detail['ref_id']}]",
                status_text,
                f"{detail['similarity']:.2f}",
                detail["context"][:50] + "..."
            )

        console.print(table)
        console.print(f"\n总结: {result['total']} 个引用中有 {result['suspicious']} 个可疑")


if __name__ == "__main__":
    cli()
