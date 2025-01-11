# Use Python slim as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies (if any)
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the script
CMD ["python", "main.py"]
