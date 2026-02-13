sync-deps:
    uv sync

run:
    uv run -m rene

test:
    uv run pytest

lint:
    uvx ruff check --fix

format:
    uvx ruff format

check-types:
    uvx ty check
