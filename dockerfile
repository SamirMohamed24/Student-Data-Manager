FROM python:3.9-slim-buster

WORKDIR /app

RUN mkdir app_files

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY student_image.jpg ./app_files/
COPY student_app.py ./app_files/

EXPOSE 1717

CMD ["python", "./app_files/student_app.py"]
