# METR CLI

## Overview

METR_CLI is a command line interface for easily creating, developing, and submitting tasks made with the [METR Task Standard](https://github.com/METR/task-standard).

Additionally, this project contains Python packages and utilities for developing METR tasks with Python. (Eventually, these will be separated into their own python pacakge)

**Background**

[METR](https://metr.org/) is an organization studying on the science of evaluating the capabilities and tendencies of state-of-the-art AI models.

The goal of the [METR Task Standard](https://github.com/METR/task-standard) is to define a common format for such tasks, so that everyone can evaluate their agents on tasks developed by other parties, rather than just their own. Making and validating informative tasks is a large amount of work, so de-duplicating efforts is important for the overall evals ecosystem. More info [here](https://github.com/METR/task-standard).



## 1 Motivation and Note to METR

Back in spring of 2024, Gatlen Culp and other MAIA members participated in a METR hackathon. Repoitory kind of scuff. (TODO: Write this)

## 2 Setup
1. Install metr-cli `pip install metr-cli`
2. Create your METR task from our template `metr task create <dir/to/clone/to> --name <task_family_name> --type <task_type=swe,cybersecurity,etc.>`
3. Make sure [docker](https://www.docker.com/) is running (install if you haven't already)
4. Test that everything is working with Docker, your task, and the CLI, `metr task run <dir/containing/task_family> addition` (addition is a predefined task in our template)
5. Develop your task, following METR's task standard documentation (https://github.com/METR/task-template)

### Requirements

* Python 3.10+
  * Pydantic (Data Validation + Better Objects)
  * Clicker (CLI interface library)
  * Rich (Higher-Quality Console Interfaces)
  * Cookiecutter (Project Templating Software)
* Node and NPM
* Docker

## 3 Development Workflow
0. Make sure the project is working locally by running the entrypoint in the development repository `python3.10 ./src/metr/metr_cli.py run ./examples/my_task/ addition`
1. Build the project using `pyproject.toml` -- `python -m build` which will save a source dist and compiled dist to `METR_CLI/dist`
2. Install the wheel package `pip install ./dist/metr_cli-0.0.1-py3-none-any.whl --force-reinstall`
3. Test that cli is available from your shell `metr` (should return usage info)
4. Test other `metr` commands. (Ex: `metr task run ./examples/my_task/my_task.py addition`)
5. Setup your `.pypirc` in your home directory with your pypi API key and username
6. Upload the repository `python -m twine upload dist/*`
7. Follow the setup section above to confirm everything is working.

## 4 CLI Usage

Everything is under the `metr task` command for now

4.A CREATE
---

**Create Task (Status: ✅ Working)**

```bash
metr task create <dir/to/clone/to> 
--name <task_family_name> 
--type <task_type=swe,cybersecurity,etc.>
```
This will create a template METR task in the directory you specify
- Uses the [Cookiecutter Library](https://www.cookiecutter.io/)
- Future features:
  - Will walk you through setting up the METR task standard with your personal information

---
**Register Task with CLI (Status: 🤔 Hypothetical)**

```bash
metr task register <cli_task_name> <dir/containing/task_family>
```
Will register your task with the CLI as `<cli_task_name>` for easier interaction (no having to use the container name) and cleanup.
- Future features
  - Also be able to register an agent for easier development

4.B DEVELOP
---

**Run Task (Status: ✅ Working)**
```bash
metr task run <dir/containing/task_family> <task_name>
```
Launches your task in a Docker container for an agent to complete

Run tests in a task environment
   - npm: 
     - All tests: `npm run test -- "taskFamilyDirectory" "taskName" "testFileName"`
     - Single test: `npm run test -- "taskFamilyDirectory" "taskName" "testFileName::testName"`
   - CLI: 
     - All tests: `metr task test <task_family_directory> <task_name> <test_file>`
     - Single test: `metr task test <task_family_directory> <task_name> <test_file> --test-name <test_name>`

---
**Run Agent to Complete Task (Status: 🦴 Skeleton Code)**
```bash
metr task run-agent "<container_name> <standard_agent_name|path/to/agent>:<path/in/VM> [start_agent_command]"
```
Run an agent inside a task environment to complete the task.

---
**Score Task (Status: 🦴 Skeleton Code)**
```bash
metr task score <container_name>
```
Scores the outcome of a task according to your TaskFamily's scoring function.
- Future features
  - Instead of having to specify a container name, the CLI will keep track of the running container, properly running, stopping, scoring, or running an agent within it given only the name of the TaskFamily.

---
**Destroy Task  (Status: 🦴 Skeleton Code)**
```bash
metr task destroy <task_environment_identifier>
```
Deletes the task container for cleanup

---
**Export Files from Container (Status: 🦴 Skeleton Code)**
```bash
metr task export <container_name> <file1> <file2> ...
```
Export files from a task container to (your local codebase?)


(C) SUBMIT
---

**Validate Task (Status: 🤔 Hypothetical)**
```bash
metr task validate <task/project/dir>
```
Will run various tests to confirm that the project is ready for submission to METR
- Checks that `eval_info.json` is configured
- Checks task docs are configured (`detail.md`, `summary.md`)
- Checks that qa docs are configured (`qa/progress.md`, `qa/qa.json`, `review.md`)
- Checks that the task can be launched properly and that there are no issues
- Checks that the repository remote is NOT public (ex: a GitHub repository anyone can check)
- Test connection to METR's submission endpoint

---
**Package Task (Status: 🤔 Hypothetical)**
```bash
metr task package <input/task/project/dir> <ouput/task/package/dir>
```
Packages your METR task into an encrypted tar file for submission. Runs `metr task validate` prior to submitting

---
**Submit Task (Status: 🤔 Hypothetical)**
```bash
metr task submit <task/package/file>
```
Submits your METR task file to METR's submission endpoint

## 5 Python Package Usage

### 5.A `metr.core`

The `metr.core` package contains


## Recommendations on How to Maintain

## Worries

### Known Issues


# Mapping of npm functions to CLI functions

Note: The `metr task create` command doesn't directly map to an npm function. It's a custom command for creating new task definitions in your project structure.