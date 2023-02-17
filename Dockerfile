FROM ubuntu:20.04

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3.8\
                                         python3-pip\
                                         software-properties-common\
                                         sqlite3 

RUN add-apt-repository ppa:mozillateam/ppa && echo '\
                                               Package: *\
                                               Pin: release o=LP-PPA-mozillateam\
                                               Pin-Priority: 1001\
                                               ' | tee /etc/apt/preferences.d/mozilla-firefox &&\
                                               apt-get install -y firefox
                                               
RUN pip3 install cryptography==38\
                 pyopenssl==22\
                 fastapi\
                 typing\
                 uvicorn\
                 facebook_page_scraper\
                 sqlalchemy

COPY database.py main.py models.py fb_pages.db ./

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]