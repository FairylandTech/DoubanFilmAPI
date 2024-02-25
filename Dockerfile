FROM python:3.9
LABEL authors="Austin[https://github.com/AustinFairyland]"
ENTRYPOINT ["top", "-b"]
WORKDIR /application
ADD . /application
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]
