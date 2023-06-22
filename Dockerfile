# Use the official Python image as the base image
FROM python:3.11-slim

# Set environment variables
ENV PIP_NO_CACHE_DIR=1

# Install Poetry
RUN pip install "poetry==1.5.1"

# Set working directory
WORKDIR /app

# Copy the necessary files to the container
COPY pyproject.toml poetry.lock /app/
COPY data/schema.sql /app/data/schema.sql
COPY trade_executor /app/trade_executor
COPY README.md /app/README.md

# Install the application dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Set the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
