FROM python:3.8
COPY requirements.txt /storeapp/requirements.txt
WORKDIR /storeapp
RUN pip install -r requirements.txt
COPY . /storeapp
ENTRYPOINT ["python"]
CMD ["app.py"]