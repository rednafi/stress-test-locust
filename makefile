.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

.PHONY: venvcheck ## Check if venv is active
venvcheck:
ifeq ("$(VIRTUAL_ENV)","")
	@echo "Venv is not activated!"
	@echo "Activate venv first."
	@echo
	exit 1
endif

install: venvcheck  ## Install the dependencies
	@pip install -r requirements.txt

lint: venvcheck		## Run Black and Isort linters
	@black .
	@isort .

upgrade: venvcheck	## Upgrade the dependencies
	@poetry update && poetry export  -f requirements.txt -o requirements.txt --without-hashes

downgrade: venvcheck ## Downgrade the dependencies
	git checkout requirements.txt
