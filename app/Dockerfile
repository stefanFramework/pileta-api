FROM python:2.7

WORKDIR /app

# Copy the current directory (.), into a container in /app/src
COPY . /app

# Runs the first command, INSIDE the container --> WORKDIR app/requirements ...
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "run.py"]