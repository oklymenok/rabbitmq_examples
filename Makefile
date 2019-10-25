.PHONY: lint test

DEBUG_BUILD=0

ifeq ($(DEBUG_BUILD),1)
    SILENCER :=
else
    SILENCER := @
endif

lint:
	${SILENCER}echo "Running linter"

test:
	${SILENCER}echo "Running tests"

venv:
	${SILENCER}virtualenv .venv && source .venv/bin/activate && pip install pika

activate-venv:
	${SILENCER}source .venv/bin/activate
