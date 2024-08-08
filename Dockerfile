FROM python:3.11

RUN mkdir -p /home/license-app

COPY . /home/license-app/

RUN pip install --upgrade pip
RUN pip install -r /home/license-app/requirements.txt
RUN pip install mysql-connector-python

WORKDIR /home/license-app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]