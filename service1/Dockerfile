FROM python:latest

RUN curl -sL https://github.com/openfaas/faas/releases/download/0.9.14/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog

#if python:latest then is better to use python3 than python2

ENV fprocess="python3 entrypoint.py"
COPY entrypoint.py /

EXPOSE 8080
CMD [ "fwatchdog" ]
