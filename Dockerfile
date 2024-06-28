FROM python:3.12-slim
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
EXPOSE 3000
CMD pip install tensorflow && python app.py



