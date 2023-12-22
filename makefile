path := .

define Comment
	- Run `make help` to see all the available options.
	- Run `make lint` to run the linter.
	- Run `make lint-check` to check linter conformity.
	- Run `dep-lock` to lock the deps in 'requirements.txt' and 'requirements-dev.txt'.
	- Run `dep-sync` to sync current environment up to date with the locked deps.
endef


.PHONY: lint
lint: ruff-check ruff-format mypy	## Apply all the linters.


.PHONY: lint-check
lint-check:  ## Check whether the codebase satisfies the linter rules.
	@echo
	@echo "Checking linter rules..."
	@echo "========================"
	@echo
	@ruff check $(path)
	@echo 'y' | mypy $(path) --install-types


.PHONY: ruff-check
ruff-check: ## Apply ruff-check.
	@echo
	@echo "Applying ruff-check..."
	@echo "======================"
	@echo
	@ruff check --fix $(path)
	@echo


.PHONY: ruff-format
ruff: ## Apply ruff-format.
	@echo "Applying ruff-format..."
	@echo "======================="
	@echo
	@ruff format $(path)


.PHONY: mypy
mypy: ## Apply mypy.
	@echo
	@echo "Applying mypy..."
	@echo "================="
	@echo
	@mypy $(path)


.PHONY: help
help: ## Show this help message.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: test
test: ## Run the tests against the current version of Python.
	pytest -v -s


.PHONY: dep-lock
dep-lock: ## Freeze deps in 'requirements.txt' file.
	@pip-compile requirements.in -o requirements.txt --no-emit-options
	@pip-compile requirements-dev.in -o requirements-dev.txt --no-emit-options


.PHONY: dep-sync
dep-sync: ## Sync venv installation with 'requirements.txt' file.
	@pip-sync
