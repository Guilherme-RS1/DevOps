FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install "fastapi[standard]" uvicorn

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]




# FROM python:3

# WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 80
# CMD [ "fastapi", "dev", "main.py", "80" ]