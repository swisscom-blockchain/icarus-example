FROM python:alpine
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY server.py ./

ENV FLASK_APP=server.py
EXPOSE 8080
ENTRYPOINT ["python", "./server.py"]
