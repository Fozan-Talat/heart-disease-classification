FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ["model_xgb.bin", "heart_disease_model.bin","modeling.py","predict.py","train.py","udfs.py","web_service.py",  "./"]

EXPOSE 7860

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:7860", "web_service:app"]