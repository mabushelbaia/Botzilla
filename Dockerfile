FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the source code
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

# Run the application
CMD ["python", "bot.py"]
