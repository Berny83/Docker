ARG DEBIAN_FRONTEND=noninteractive
FROM debian:latest
LABEL maintainer="aagrivan"
ENV TS3SERVER_LICENSE=accept
# accept the teamspeak license
WORKDIR /home/teamspeak
# указывает директорию откуда будет выполняться команда
EXPOSE 9987/udp 10011 30033
# 9987 default voice
# 10011 server query
# 30033 file transport
RUN apt-get update -y && \
		apt-get upgrade -y && \
		apt-get install -y wget bzip2 && \
		wget https://files.teamspeak-services.com/releases/server/3.12.1/teamspeak3-server_linux_amd64-3.12.1.tar.bz2 && \
		tar -xvf teamspeak3-server_linux_amd64-3.12.1.tar.bz2
WORKDIR teamspeak3-server_linux_amd64
ENTRYPOINT sh ts3server_minimal_runscript.sh
# ENTRYPOINT ["sh", "ts3server_minimal_runscript.sh"]