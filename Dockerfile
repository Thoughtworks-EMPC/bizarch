FROM python:3.7

WORKDIR /usr/src/bizarch

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app app
COPY data data
COPY log log

CMD [ "python3", "-m", "app", "clear"]