FROM python:latest

WORKDIR /graphql-server

EXPOSE 8080

RUN pip install 'strawberry-graphql[debug-server]'

COPY server .

CMD [ "strawberry", "server", "server" ]