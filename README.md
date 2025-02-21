# Project setup

## Setup `uv` globally
https://docs.astral.sh/uv/getting-started/installation/ 

## Install dependencies
```bash
  uv sync
```

## Format
```bash
  uv run black --verbose .
```

## Test
```bash
  uv run pytest
```

## Run
```bash
  uv run fastapi dev --reload
```
