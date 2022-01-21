FROM python:3.7.6-stretch
COPY . /
WORKDIR /
RUN python -m venv venv
CMD . venv/Scripts/activate && exec python app.py