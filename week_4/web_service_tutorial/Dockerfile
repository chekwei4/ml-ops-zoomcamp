FROM python:3.8.13-slim

RUN pip install -U pip

WORKDIR /app

COPY [ "requirements.txt", "./" ]

RUN pip3 install -r requirements.txt

COPY [ "lin_reg.bin", "predict.py", "./" ]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]