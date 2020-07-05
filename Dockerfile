FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /opt

COPY . /opt

VOLUME /opt

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

EXPOSE 80
# CMD ["python", "/opt/manage.py", "runserver", "0.0.0.0:80"]
CMD ./startup.sh
# docker build -t match . && docker run -p 8000:80 -v /opt/match_score:/opt --name match match