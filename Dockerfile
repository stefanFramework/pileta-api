FROM python:3.7-slim

WORKDIR /src

COPY . /src

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "src/app/routes/test/test.py"]