# Step 1: Use a Python base image
FROM python:3.9-slim

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy the requirements file and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of the application files
COPY . /app

# Step 5: Expose the Flask app's port
EXPOSE 5000

# Step 6: Run the application
CMD ["python", "app/app.py"]
