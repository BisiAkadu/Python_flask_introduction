FROM python:alpine
ADD . /app
WORKDIR /app
COPY requirement.txt .
RUN pip install --upgrade pip
RUN pip install -r requirement.txt
COPY . .
EXPOSE 5002
CMD ["python", "main.py"]