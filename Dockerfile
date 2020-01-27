FROM python:3.7-alpine

RUN mkdir -p /usr/src/awsctl

WORKDIR /usr/src/awsctl

COPY requirements.txt /usr/src/awsctl

RUN pip install

COPY . /usr/src/awsctl

ENTRYPOINT [ "python", "./awsctl.py" ]

CMD [ "./awsctl.py" ]
