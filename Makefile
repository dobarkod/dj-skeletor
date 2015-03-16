FLAKE8_MAX_COMPLEXITY=10
FLAKE8_IGNORE=E128,E131
FLAKE8_OPTS=--exclude=.git,migrations --max-complexity=$(FLAKE8_MAX_COMPLEXITY) --ignore=$(FLAKE8_IGNORE)

.PHONY: test coverage

help:
	@echo "Available commands:"
	@echo "    test - run the tests"
	@echo "    coverage - run the test and compute code coverage"
	@echo "    lint - run the source code / style checker"
	@echo "    update - update database and static assets"
	@echo "    prod-depends - install production dependencies"
	@echo "    dev-depends - install development dependencies"
	@echo "    test-depend - install test dependencies"
	@echo "    dev-update - update dev deps, database and static assets"
	@echo "    clean - remove .pyc files"
all:
	test

clean:
	find . -name '*.pyc' -delete

test: clean
	python manage.py test --settings=project.settings.test

coverage: clean
	coverage run --source=. manage.py test --settings=project.settings.test
	coverage html
	coverage report
	@echo "HTML report available in 'htmlcov/' directory."

lint:
	flake8 $(FLAKE8_OPTS) .

dev-depends:
	pip install -r requirements/dev.txt

test-depends:
	pip install -r requirements/test.txt

prod-depends:
	pip install -r requirements/prod.txt

dev-update: dev-depends
	$(MAKE) update

update: clean
	python manage.py migrate
	python manage.py collectstatic --noinput
