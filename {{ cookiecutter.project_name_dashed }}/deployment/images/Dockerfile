###################################################
#   Stage 1: Get poetry                           #
###################################################
FROM python:{{ cookiecutter.python_version }}-slim AS poetry

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential \
curl \
&& rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
ln -s /root/.local/bin/poetry /usr/local/bin/poetry

###################################################
#   Stage 2: Get deps                             #
###################################################
FROM poetry AS builder

# Set work directory
WORKDIR /app

# Copy poetry configuration
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main

# Copy the rest of the application code
COPY . /app/

###################################################
#   Stage 3: Create user and run                  #
###################################################
FROM python:{{ cookiecutter.python_version }}-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy dependencies from builder
COPY --from=builder /app /app

# Create and switch to a non-root user
RUN addgroup --system app && adduser --system --ingroup app app
RUN chown -R app:app /app
USER app

# Set labels for the Docker image
LABEL org.opencontainers.image.title="{{ cookiecutter.project_name }}"
LABEL org.opencontainers.image.description="{{ cookiecutter.short_description }}"
LABEL org.opencontainers.image.version="0.1.0"
LABEL org.opencontainers.image.authors="{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.source="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name_dashed }}"
LABEL org.opencontainers.image.url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name_dashed }}"
LABEL org.opencontainers.image.documentation="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name_dashed }}/blob/main/README.md"
LABEL org.opencontainers.image.vendor="{{ cookiecutter.github_username }}"

# Expose port (if your application uses a specific port, adjust accordingly)
# EXPOSE 8000

# Define the entry point to the console script
ENTRYPOINT ["python" , "{{ cookiecutter.project_name_underscored }}/main.py"]

# Optional: Specify default command arguments
# CMD []
