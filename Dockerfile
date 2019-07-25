#This is a sample Image 
FROM ubuntu 
MAINTAINER   estsb@gmail.com 


RUN apt update

RUN apt-get install -y python3


RUN apt-get install -y python3-pip

RUN apt-get install -y unoconv


COPY sketchToHtml /sketchToHtml


RUN cd /sketchToHtml/sketch_code && ls && pip3 install -r requirements.txt && pip3 install django==1.11.20

EXPOSE 8080
RUN apt update && apt install -y libsm6 libxext6
RUN apt-get install -y libxrender1
RUN apt-get install -y build-essential
RUN apt-get install -y python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev  libdc1394-22-dev 
RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN cd /sketchToHtml/sketch_code/scripts && sh get_data.sh && sh get_pretrained_model.sh
ENTRYPOINT ["python3", "/sketchToHtml/web_app/manage.py", "runserver","0.0.0.0:8080"]


 


