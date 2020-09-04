#!/bin/bash
function check_venv() {
    """Check whether virtual environment is active."""
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        INVENV=1
    else
        INVENV=0
    fi
}

function install_black() {
    local FILE=/venv/bin/black
    if [[ -f "$FILE" ]]; then
        true
    else
        echo "Installing black..."
        pip install black
    fi
}

function install_flake8() {
    local FILE=/venv/bin/flake8
    if [[ -f "$FILE" ]]; then
        true
    else
        echo "Installing flake8..."
        pip install flake8
    fi
}

function install_isort() {
    local FILE=./venv/bin/isort
    if [[ -f "$FILE" ]]; then
        true
    else
        echo "Installing isort..."
        pip install isort
    fi
}

function run_black() {
    echo "Applying Black..."
    black .
}

function run_flake8() {
    echo "Applying Flake8"
    flake8 .
}

function run_isort() {
    echo "Applying Isort"
    isort .
}

check_venv

if [[ $INVENV == 1 ]]; then
    install_black
    install_flake8
    install_isort

    run_black
    run_flake8
    run_isort

else

    echo "Virtual environment is not active. Activate the venv and then run again!"
    exit
fi
