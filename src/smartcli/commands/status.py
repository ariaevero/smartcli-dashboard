import typer
import psutil

def status():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    typer.echo(f"🖥️ CPU Usage: {cpu}%")
    typer.echo(f"💾 Memory Usage: {mem}%")
    typer.echo(f"📀 Disk Usage: {disk}%")
