# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy all files
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the ports for API and chat interface
EXPOSE 5000 5001

# Start both the API and chat interface (using gunicorn or supervisor in production)
# For simplicity, we use a shell script to start both services concurrently.
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:5000 api.app:app & gunicorn --bind 0.0.0.0:5001 chat_interface.chat:app"]
