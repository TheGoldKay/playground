#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <level_number>"
    exit 1
fi

if ! [[ $1 =~ ^[0-9]+$ ]]; then
    echo "Error: Please provide a valid number"
    exit 1
fi

ssh "bandit$1@bandit.labs.overthewire.org" -p 2220