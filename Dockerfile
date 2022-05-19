FROM python:3.8-slim-buster

# setup dependencies
RUN apt-get update
RUN apt-get install xz-utils
RUN apt-get -y install curl git
RUN pip install pyyaml
RUN pip install requests
RUN pip install python-dateutil
RUN pip install pandas

WORKDIR /usr/src/app/

COPY . .

#RUN git clone https://github.com/SigmaHQ/sigma.git
RUN cp devo-win.yml sigma/tools/config/
RUN mkdir Translations
RUN python translate.py
RUN mv Devo_* Translations
RUN python main.py

CMD ["sh"]
