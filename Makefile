.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: run-server
run-server:
	poetry run python -m manage runserver

.PHONY: migrations
migrations:
	poetry run python -m manage makemigrations


.PHONY: migrate
migrate:
	poetry run python -m manage migrate

.PHONY: superuser
superuser:
	poetry run python -m manage createsuperuser

.PHONY:
startapp:
	poetry run python -m manage startapp $(ARGS)

.PHONY: update
update: install, migrate;
