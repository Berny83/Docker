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

# How to build it?
# docker build -f ../School21/Docker/01_dockerfiles/00/Dockerfile -t ex00 .
# --tag, -t - Name and optionally a tag in the ‘name:tag’ format
# --file, -f - Name of the Dockerfile (Default is ‘PATH/Dockerfile’)
# “.” - построить образ здесь
# How to run it?
# docker run --rm -ti ex00

# Dockerfile – это сценарий, который состоит из последовательности команд и аргументов, необходимых для создания образа. Такие сценарии упрощают развёртывание и процесс подготовки приложения к запуску.

# Сначала Dockerfile определяет образ, на основе которого будет происходить сборка. Затем идёт ряд методов, команд и аргументов, которые создадут новый образ.
