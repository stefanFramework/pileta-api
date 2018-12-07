FROM python:3.7-slim

WORKDIR /app

# Copy the current directory (.), into a container in /app/src
COPY . /app

# Runs the first command, INSIDE the container --> WORKDIR app/requirements ...
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "src/app/routes/v1/main.py"]