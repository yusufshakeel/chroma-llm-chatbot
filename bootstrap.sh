#!/usr/bin/env sh

echo "Creating documents folder if it does not exist."
mkdir -p documents

echo "Creating models folder if it does not exist."
mkdir -p models

echo "Creating .env file from .env.example"
cp .env.example .env
