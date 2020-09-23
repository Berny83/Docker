#ARG VERSION=latest
#FROM alpine:$VERSION
#defines a variable that users can pass at build-time to the builder with the docker build command
FROM alpine:latest
#определяем базовый/родительский образ для начала процесса построения контейнера
#MAINTAINER aagrivan - устарело в пользу LABEL
LABEL maintainer="aagrivan"
#позволяет добавлять в образ метаданные.
RUN apk update && \
		apk upgrade && \
		apk add vim
ENTRYPOINT ["vim"]
#ENTRYPOINT vim
#has two forms: exec form (preferred) and shell form
#устанавливает конкретное приложение по умолчанию, которое используется каждый раз в момент построения контейнера с помощью образа.