FROM python:3.9-slim

COPY . .
RUN python3 -m pip install -U --no-cache-dir -r requirements.txt

CMD [ "python3", "main.py" ]