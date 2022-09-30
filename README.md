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

## Configuration options

(Use these values to configure the `config.yml` file)

### Reason options

38663537-3261-3233-2d31-3033352d3431 - Urgence mineure

31653438-3432-3237-2d34-3062652d3436 - Consultation prioritaire

66316339-3434-3431-2d39-3464612d3463 - Suivi périodique ou préventif

39333631-3230-3732-2d63-6362372d3461 - Suivi régulier

66653736-3031-3266-2d34-3336312d3462 - Suivi de grossesse

33363931-6230-3034-2d37-6638392d3432 - Suivi d’un enfant de 0 à 5 ans

### Perimeter options

"0" = 0 à 10 km

"1" = 10 à 20 km

"2" = 20 à 30 km

"3" = 30 à 40 km

"4" = 40 à 50 km