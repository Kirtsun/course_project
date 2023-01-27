FROM python:3.10

RUN apt update && apt install curl -y

COPY shop/requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY wait-for-command.sh /

COPY shop app/

WORKDIR app/

EXPOSE 8000

RUN chmod +x docker-entrypoint.sh /wait-for-command.sh runserver.sh

#ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]