FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the port your app runs on
ENV PORT=5000
EXPOSE $PORT

# Start the application
CMD ["sh", "-c", "gunicorn run:app --bind 0.0.0.0:$PORT"]
