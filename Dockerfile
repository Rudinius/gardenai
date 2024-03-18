FROM python:3.12.2

COPY . /app/

WORKDIR /app

RUN python -m pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "client.py", "--server.port=8501", "--server.address=0.0.0.0"]