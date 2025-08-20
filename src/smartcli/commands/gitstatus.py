import typer
import subprocess

def gitstatus():
    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
        status = subprocess.check_output(["git", "status", "--short"]).decode().strip()
        typer.echo(f"🌿 Current branch: {branch}")
        typer.echo("📄 Changes:\n" + (status if status else "No changes"))
    except subprocess.CalledProcessError:
        typer.echo("❌ Not a Git repository.")
