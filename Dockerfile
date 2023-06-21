# Use the official Python image as the base image
FROM python:3.11-slim

# Set environment variables
ENV PIP_NO_CACHE_DIR=1  \
    QUANTITY="5000" \
    PRICE="230" \
    SYMBOL="bnbusdt" \
    EXCHANGE="bid"

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
CMD [ "poetry", "run", "python", "trade_executor/main.py", "-q", "5000", "-p", "230" ]

#RUN chmod +x /app/entrypoint.sh
#ENTRYPOINT ["/app/entrypoint.sh"]
