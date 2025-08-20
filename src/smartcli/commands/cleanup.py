import typer
import os

def cleanup():
    """Simulates cleanup of temporary files."""
    temp_dir = os.getenv('TEMP') or '/tmp'
    typer.echo(f"🧹 Cleaning up temporary files in {temp_dir}...")
    # Simulated cleanup logic
    typer.echo("✅ Cleanup complete.")
