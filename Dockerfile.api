FROM python:3.7.7

WORKDIR /app

# Copy the current directory (.), into a container in /app
COPY ./app /app

# Runs the first command, INSIDE the container --> WORKDIR app/requirements ...
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN ["chmod", "+x", "entrypoint.sh"]

ENTRYPOINT ["sh", "entrypoint.sh" ]

CMD ["start", "development"]

EXPOSE 80