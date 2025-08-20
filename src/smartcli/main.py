import typer
from smartcli.dashboard import launch_dashboard
from smartcli.commands.status import status
from smartcli.commands.cleanup import cleanup
from smartcli.commands.gitstatus import gitstatus
from smartcli.commands.summarize import summarize

app = typer.Typer()


@app.command()
def dashboard():
    """Launches the Streamlit dashboard."""
    subprocess.run(["streamlit", "run", os.path.join(os.path.dirname(__file__), "dashboard.py")])

@app.command()
def greet(name: str):
    typer.echo(f"Hello, {name}!")

@app.command()
def dashboard():
    launch_dashboard()

@app.command(name="status")
def status_command():
    status()

@app.command(name="cleanup")
def cleanup_command():
    cleanup()

@app.command(name="gitstatus")
def gitstatus_command():
    gitstatus()

@app.command(name="summarize")
def summarize_command(file: str):
    summarize(file)

if __name__ == "__main__":
    app()
