FROM python:3.11-bookworm

# It allows for log messages to be dumped into the stream immediately instead of being buffered.
ENV PYTHONUNBUFFERED=1
ENV TZ="Asia/Tokyo"

WORKDIR /src

RUN pip install poetry

# If poetry files exist
COPY pyproject.toml* poetry.lock* ./

# If pyproject.toml file already exists, install libraries.
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

ENTRYPOINT poetry run uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload