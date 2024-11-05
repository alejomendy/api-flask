FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Start the application
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:5000"]