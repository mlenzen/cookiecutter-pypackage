.PHONY: docs test

help:
	@echo "  clean       remove unwanted files like .pyc's"
	@echo "  lint        check style with flake8"
	@echo "  tests       run tests (using py.test)"
	@echo "  testall     run tests for all Python versions (using tox)"
	@echo "  coverage    run coverage report"
	@echo "  publish     publish to PyPI"
	@echo "  docs        create HMTL docs (using Sphinx)"

tests:
	python setup.py test

testall:
	tox

clean:
	rm -rf build
	rm -rf dist
	rm -rf {{ cookiecutter.repo_name|replace('-', '_') }}.egg-info
	find . -name *.pyc -delete
	find . -name *.pyo -delete
	find . -name *~ -delete
	find . -name __pycache__ -delete

lint:
	flake8 {{ cookiecutter.repo_name|replace('-', '_') }} tests

coverage:
	coverage run --source {{ cookiecutter.repo_name|replace('-', '_') }} setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

publish:
	python setup.py sdist upload
	python setup.py bdist_wheel upload

docs:
	rm -f docs/{{ cookiecutter.repo_name|replace('-', '_') }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.repo_name|replace('-', '_') }}
	make -C docs clean
	make -C docs html
	open docs/_build/html/index.html
