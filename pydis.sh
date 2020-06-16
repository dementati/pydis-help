#!/bin/bash
cd "$(dirname "$0")"
PIPENV_VERBOSITY=-1 pipenv run python main.py $@
