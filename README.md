# Overview

poetry build
pip install ./dist/metr_cli-0.0.1-py3-none-any.whl --force-reinstall
metr
metr task run ./examples/my_task/my_task.py addition
python3.10 ./src/metr/metr_cli.py run ./examples/my_task/ addition

A CLI interface for the METR task standard. The METR task standard is a way

This project was generated with [cookiecutter](https://github.com/audreyr/cookiecutter)

TODO: Make a METR package with all the proper types so you can import it without the full directory

## Setup

### Requirements

* Python 3.11+

### Installation

Install it directly into an activated virtual environment:

```text
$ pip install metr-cli
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add metr-cli
```

## Usage

Everything is under the `metr` command

### 1 Tasks

`metr task create <path> --name test_task --type test`
- This uses cookiecutter to create a new task in the current director

`metr task run <task_path>`
- Runs the current task using Docker

`metr task validate <task_path>`
- Will run various tests to confirm that the project is ready for publishing
  - Tests if QA is set up well
  - Tests if

# Mapping of npm functions to CLI functions

1. Create a task environment
   - npm: `npm run task -- "taskFamilyDirectory" "taskName"`
   - CLI: `metr task run <task_family_directory> <task_name>`

2. Run an agent inside a task environment
   - npm: `npm run agent -- "[docker container name]" "path/to/agent[:path/in/VM]" "command to start agent"`
   - CLI: `metr task agent <container_name> <agent_path> <start_command>`

3. Score a task environment
   - npm: `npm run score -- [docker container name]`
   - CLI: `metr task score <container_name>`

4. Export files from a task environment
   - npm: `npm run export -- [docker container name] [file1] [file2] ...`
   - CLI: `metr task export <container_name> <file1> <file2> ...`

5. Run tests in a task environment
   - npm: 
     - All tests: `npm run test -- "taskFamilyDirectory" "taskName" "testFileName"`
     - Single test: `npm run test -- "taskFamilyDirectory" "taskName" "testFileName::testName"`
   - CLI: 
     - All tests: `metr task test <task_family_directory> <task_name> <test_file>`
     - Single test: `metr task test <task_family_directory> <task_name> <test_file> --test-name <test_name>`

6. Destroy a task environment
   - npm: `npm run destroy -- "taskEnvironmentIdentifier"`
   - CLI: `metr task destroy <task_environment_identifier>`

Note: The `metr task create` command doesn't directly map to an npm function. It's a custom command for creating new task definitions in your project structure.