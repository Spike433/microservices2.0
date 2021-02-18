FROM python:latest

RUN curl -sL https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog

#Should be pythonVersion, not python

ENV fprocess="python3 entrypoint.py"
COPY entrypoint.py /

RUN pip install requests

EXPOSE 9000            

#cant have 2 containers on same port

CMD [ "fwatchdog" ]
