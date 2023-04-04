FROM python:3

WORKDIR /usr/src/app

COPY semantic.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install spacy

CMD ["python", "./semantic.py"]