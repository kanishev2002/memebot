FROM pypy:3.8-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["pypy", "./main.py"]