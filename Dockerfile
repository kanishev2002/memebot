FROM pypy:3.8-slim

WORKDIR /usr/src/app

ENV TOKEN=5033731488:AAEaZAaAbngmoWkW7KRGz-2hr84gBmAI8mY

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["pypy", "./main.py"]