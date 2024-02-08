#==============×==============#
#      Created by: Alfa-Ex
#=========× Sanzydev ×=========#
# Izzy Ganteng

FROM sanzydev/sanzy:xd

RUN git clone -b Sanzy-Userbot https://github.com/sanzydev/Sanzy-Userbot /home/sanzyuserbot/ \
    && chmod 777 /home/sanzyuserbot \
    && mkdir /home/sanzyuserbot/bin/

#COPY ./sample.env ./.env* /home/sanzyuserbot/

WORKDIR /home/sanzyuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
