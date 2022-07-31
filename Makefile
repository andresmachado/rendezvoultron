help:
	@echo "make init - install virtual environment(required for the other targets)"
	@echo "make -s install - install packages"
	@echo "make -s test - run unit tests"
	@echo "make -s run - run the main script"
	@echo "-s option hides the Make invocation command."

venv:
	test -d venv || virtualenv venv
	@echo "Activate your virtual environment by running:"
	@echo "source venv/bin/activate"

init: venv

install:
	pip install -Ur requirements.txt

doctest:
	# @python -m doctest main.py -v
	@echo "Starting doctest...(no output means no failures)"
	@python -m doctest main.py

pytest:
	@python -m pytest

test: doctest pytest

testWithCoverage:
	@python -m coverage run -m doctest main.py

coverageTerminal: testWithCoverage
	@echo ===== doctest coverage report =====
	@python -m coverage report
	@python -m pytest --cov-report term-missing --cov .


coverageDoctestHtml: testWithCoverage
	python -m coverage html
	open htmlcov/index.html

coveragePytestHtml: testWithCoverage
	python -m pytest --cov-report html --cov .
	open htmlcov/index.html

clean:
	test -f .coverage && rm .coverage || true
	test -d htmlcov && rm -rf htmlcov || true
	@echo ".coverage and htmlcov deleted"

run:
	@python main.py

.PHONY: help venv init clean install test doctest pytest run
