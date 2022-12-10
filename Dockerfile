FROM python:3.11.1-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .

ENTRYPOINT [ "python" ]
CMD ["main.py" ]