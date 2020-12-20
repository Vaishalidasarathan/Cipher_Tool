FROM python:3.7

ADD CipherTool.py /

RUN pip install secretpy \
    && pip install console-menu

CMD [ "python", "./CipherTool.py" ]
