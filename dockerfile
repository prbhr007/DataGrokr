FROM python:2.7-alpine
RUN pip install boto3 
RUN mkdir /app
WORKDIR /app
RUN mkdir ~/.aws
RUN echo "[default]" > ~/.aws/config
RUN echo "[default]" > ~/.aws/credentials
RUN echo "aws_secret_access_key = XXX" >> ~/.aws/credentials
RUN echo "aws_access_key_id = XXX" >> ~/.aws/credentials
COPY hello.py /app
