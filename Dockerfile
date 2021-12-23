FROM pypy:3.8-slim

WORKDIR /usr/src/app

ENV TOKEN=5033731488:AAEaZAaAbngmoWkW7KRGz-2hr84gBmAI8mY

COPY . .

RUN pip install --no-cache-dir pyTelegramBotAPI

ENTRYPOINT ["pypy", "./main.py"]