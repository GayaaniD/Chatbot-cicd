# Stage 1: Install system dependencies
ARG PYTHON_VERSION=3.11.6
FROM python:${PYTHON_VERSION}-slim AS base

# Set environment variables
# New style (single string with “key=value”)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_NO_INTERACTION=1

# Set working directory
WORKDIR /app

# Stage 2: Install dependencies
FROM base AS dependencies

# Install Poetry
RUN pip install --upgrade pip && pip install poetry

# Copy only the dependency files
COPY pyproject.toml poetry.lock* /app/

# Install Python dependencies
# …
RUN poetry config virtualenvs.create false \
 && poetry install --no-root --only main
# …

# Stage 3: Final build
FROM dependencies AS final

# Copy the rest of the application code
COPY . /app

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", \
     "--server.port=8501", "--server.address=0.0.0.0"]
     