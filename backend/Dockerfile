FROM python:3.10-slim

WORKDIR /app

COPY reqs.txt ./

RUN pip install -r reqs.txt

COPY . .

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]