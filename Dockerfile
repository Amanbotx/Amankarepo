FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
RUN pip install google-generativeai
RUN pip install openai==0.27.0
RUN pip install git+https://github.com/MrTG-CodeBot/pyrogram.git
RUN pip install ffmpeg
RUN pip install spotipy
RUN pip install yt_dlp
RUN pip install spotdl
RUN pip install pafy
RUN pip install google-generativeai
RUN pip install pytube 
RUN pip install youtube-search
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /TheMovieProviderBot
WORKDIR /TheMovieProviderBot
COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
