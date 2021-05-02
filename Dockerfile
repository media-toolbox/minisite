FROM python:3.9.4

ENV PYTHONUNBUFFERED 1

EXPOSE 8092
WORKDIR /app

COPY . ./
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

RUN poetry install --no-dev

ENTRYPOINT ["minisite"]
