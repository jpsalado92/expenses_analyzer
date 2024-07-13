
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements-dev.txt /app
RUN python -m pip --disable-pip-version-check --no-cache-dir install -r requirements-dev.txt
RUN rm -rf /app