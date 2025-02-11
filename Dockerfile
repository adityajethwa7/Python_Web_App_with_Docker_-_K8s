FROM python:3.9-slim

WORKDIR /app

# Copy and install requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Use non-root user for security
RUN addgroup --system appuser && \
    adduser --system --ingroup appuser appuser
USER appuser

# Expose port
EXPOSE 5000

CMD ["python", "-u", "app.py"]