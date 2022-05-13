FROM python:3.10.4-alpine
WORKDIR /usr/src/app
COPY src .
RUN pip install Flask   
RUN pip install flask-cors
ENTRYPOINT [ "python", "./app.py" ]
EXPOSE 80