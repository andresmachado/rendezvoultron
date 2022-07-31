# Overview

A bot built to schedule rendez-vous on RVSQ.
It uses a Makefile to manage your workflow.

## Prerequisite

1. Make sure you have Python 3 installed.
2. Install linter pyflakes: `pip3 install --upgrade pyflakes`
3. Install code style checker pycodestyle: `pip3 install --upgrade pycodestyle`
4. Install Virtual Environment: `pip3 install virtualenv`

To keep the `Makefile` simple, it is written such that it depends on your
 virtual environment active on the current terminal. To activate run:
 `source venv/bin/activate`

You can optionally deactivate by running: `deactivate`

## Developing

Use of virtual environment is baked in the Makefile.

Run `make` to see the list of commands:

```text
@echo "make init - initialize virtual environment for you project"
@echo "make install - install packages"
@echo "make test - run unit tests"
@echo "make run - run the main script"
```

See the [Makefile](./Makefile) for the complete list

### Adding Packages

IMPORTANT: Virtual environment must be active on your shell before proceeding.

It is recommended to manually add any new package to `requirements.txt` the
 reason being the automatic approach `pip3 freeze > requirements.txt` can lead
  to a transitive dependency lingering when we update a direct dependency.

Follow the steps to add:

```bash
$ pip install new_package==1.2.3
# or you can run it without the version, but make note of the version install
# by looking at the console output.

echo "new_package=1.2.3" >> requirements.txt
```

## Unit Tests

See other templates for example.

## TODO

Automatic run tests on code change.
