# Overview

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