FROM debian:latest
LABEL maintainer="aagrivan"

ENV TERM=xterm

RUN apt-get update -y && \
		apt-get upgrade -y && \
		apt-get install -y curl openssh-server ca-certificates postfix xterm tzdata

RUN curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | bash && \
		apt-get install -y gitlab-ce
		# apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# curl -s режим тишины Не показывает индикатор выполнения и сообщения об ошибках.
# rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* - чистим кэш apt-get
		# EXTERNAL_URL="http://gitlab.example.com" && \
RUN sed -i "s/# grafana\['enable'\] = true/grafana['enable'] = false/g" /etc/gitlab/gitlab.rb && \
		sed -i "s/unicorn\['worker_timeout'\] = 60/unicorn\['worker_timeout'\] = 300/g" /etc/gitlab/gitlab.rb
# https://medium.com/@1997corry/running-your-own-gitlab-on-docker-community-edition-39c4a8f99553

EXPOSE 443 80 22

ENTRYPOINT (/opt/gitlab/embedded/bin/runsvdir-start &) && \
						gitlab-ctl reconfigure && \
						gitlab-ctl tail
						# tail -f /dev/null
#https://gitlab.com/gitlab-org/omnibus-gitlab/issues/4257

# Build Image
# docker build -t ex03 .

# Create Container
# docker run --name ex03 -it --rm -p 8080:80 -p 8022:22 -p 8443:443 --privileged ex03
# docker run --name ex03 -it --shm-size=4g --rm -p 8080:80 -p 8022:22 -p 8443:443 --privileged ex03
# посл команда выводит ошибку

# docker-machine -s "/Users/aagrivan/goinfre/.docker/machine" create --virtualbox-cpu-count="4" --virtualbox-memory "4096" --driver virtualbox Char
# docker run -it -d --rm --cpus="4.0" --memory="4g" -p 8080:80 --privileged ex03