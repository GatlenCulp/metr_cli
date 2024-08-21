import subprocess
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.absolute()
WORKBENCH_DIR = PROJECT_ROOT / "src" / "task-standard" / "workbench"

def run_npm_command(command: str, cwd: Path):
    npm_command = ["npm", "--prefix", str(WORKBENCH_DIR), "run"]
    npm_command.extend(command.split())  # Split the command into separate arguments
    
    print(f"Current working directory: {os.getcwd()}")
    print(f"Workbench directory: {WORKBENCH_DIR}")
    print(f"Full npm command: {' '.join(npm_command)}")
    
    env = os.environ.copy()
    env["INIT_CWD"] = str(cwd)
    
    try:
        result = subprocess.run(
            npm_command,
            shell=False,  # Changed to False as we're using a list of arguments
            check=True,
            cwd=cwd,
            env=env,
            capture_output=True,
            text=True
        )
        print(f"STDOUT:\n{result.stdout}")
        print(f"STDERR:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing npm command: {e}")
        print(f"STDOUT:\n{e.stdout}")
        print(f"STDERR:\n{e.stderr}")
        raise

if __name__ == "__main__":
    abs_task_family_dir = Path("/Users/hugz/Work-Projects/metr_cli/examples/days_since")
    task_name = "days_since.py"
    cmd = f"task -- {str(abs_task_family_dir)} {task_name}"
    run_npm_command(cmd, Path.cwd())