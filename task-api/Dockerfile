FROM python:3.10-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .


ENV USER_API=http://kong:8000
# ENV USER_API=http://kong:8000/services/users
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]