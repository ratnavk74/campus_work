FROM python:3.10-slim

WORKDIR /campus1

COPY . .

CMD ["python", "campus1.py"]
