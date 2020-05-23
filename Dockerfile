FROM python:3.8.0-alpine
WORKDIR /projectcode
ENV FLASK_APP ussd-app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python","ussd-app.py"]