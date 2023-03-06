FROM python:3.8

WORKDIR /opt/apps/project

COPY requirements.txt .
RUN pip install -r requirements.txt -i https://pypi.doubanio.com/simple

COPY . .

CMD ["gunicorn", "-c", "gunicorn.conf.py"]
