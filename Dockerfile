# Build stage
FROM python:3.9-slim AS builder

# Set environment variable for the file author
ENV AUTHOR="Adrian Bartoszek"

# Set working directory
WORKDIR /app

# Copy requirements.txt file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy and compile source code
COPY server.py .
RUN python -m compileall server.py

# Final stage
FROM python:3.9-slim AS final

# Copy compiled code from the build stage
COPY --from=builder /app/server.py .

# Copy requirements.txt file
COPY --from=builder /app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add curl dependency (using system command)
RUN apt-get update && apt-get install -y curl

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:5000/health || exit 1

# Run the server upon container startup
CMD ["python", "server.py"]
