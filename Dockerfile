# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Create a non-root user and set permissions
RUN useradd -m -u 1000 user && \
    mkdir -p /tmp/hf_cache && \
    chown -R user:user /tmp/hf_cache /app

# Switch to non-root user
USER user

# Set HF cache inside container
ENV HF_HUB_CACHE=/tmp/hf_cache

# Copy requirements and install
COPY --chown=user:user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY --chown=user:user . .

# Expose the port HF Spaces uses
EXPOSE 7860

# Run the Flask app
CMD ["python", "app.py"]