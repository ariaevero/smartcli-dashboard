import typer

def summarize(file: str):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        summary = content[:300] + '...' if len(content) > 300 else content
        typer.echo(f"📄 Summary of {file}:\n{summary}")
    except Exception as e:
        typer.echo(f"❌ Error: {e}")
