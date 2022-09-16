FROM python:3.7-slim

# dir for application
RUN mkdir /app

# copy all files and folder except .gitignore and Dockerfile itself
# exceptions are in .dockerignore file
COPY . /app

# install requirements
RUN pip3 install -r /app/requirements.txt --no-cache-dir

# make dir /app as work dir
WORKDIR /app

# run the server when container starts
CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
