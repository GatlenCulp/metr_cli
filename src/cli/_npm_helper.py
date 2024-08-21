import subprocess
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
WORKBENCH_DIR = PROJECT_ROOT / "src" / "workbench"

def run_npm_command(command: str, cwd: Path):
    """
    Run an npm command from the workbench directory, while maintaining the context of the current working directory.
    
    :param command: The npm command to run
    :param cwd: The current working directory where the command was initiated
    """
    workbench_dir = PROJECT_ROOT / "src" / "workbench"
    npm_command = f"npm --prefix {workbench_dir} run {command}"
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Workbench directory: {workbench_dir}")
    print(f"Full npm command: {npm_command}")
    print(f"Expected Dockerfile location: {workbench_dir.parent / 'Dockerfile'}")
    
    env = os.environ.copy()
    env["INIT_CWD"] = str(cwd)
    
    result = subprocess.run(
        npm_command,
        shell=True,
        check=True,
        cwd=cwd,
        env=env,
        capture_output=True,
        text=True
    )
    print(result.stdout)