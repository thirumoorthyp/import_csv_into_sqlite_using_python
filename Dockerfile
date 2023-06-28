FROM python:3.6
MAINTAINER Thirumoorthy "thirusece@gmail.com"
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["import_csv.py"]
