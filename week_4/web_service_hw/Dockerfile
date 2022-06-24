# FROM python:3.8.13-slim
FROM agrigorev/zoomcamp-model:mlops-3.9.7-slim

RUN pip install -U pip

WORKDIR /app

COPY [ "requirements.txt", "./" ]
RUN pip3 install -r requirements.txt

COPY [ "starter.py", "./" ]

# EXPOSE 9696

# ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]
CMD [ "python", "starter.py", "2021", "04" ]