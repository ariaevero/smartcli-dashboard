import typer
from .dashboard import launch_dashboard

app = typer.Typer()

@app.command()
def greet(name: str):
    typer.echo(f"Hello, {name}!")

@app.command()
def dashboard():
    launch_dashboard()

if __name__ == "__main__":
    app()
