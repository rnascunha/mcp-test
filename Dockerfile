# Use a lightweight Python base image
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
RUN --mount=type=bind,source=uv.lock,target=uv.lock \
  --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  uv sync

# Copy the rest of the application code into the container
COPY src/ .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application with Uvicorn
CMD ["uv", "run", "app.py", "--transport=http", "--path=/mcp","--url=0.0.0.0", "--port=8000", "--auth=api-key-12345"]