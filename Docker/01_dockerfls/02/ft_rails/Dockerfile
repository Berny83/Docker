FROM ruby:latest
LABEL maintainer="aagrivan"

# Ruby image itself is based on a Debian image, we use apt-get to install those, backend
RUN apt-get update -y && \
		apt-get upgrade -y && \
		apt-get install -y nodejs sqlite3
# sqlite3 for database, nodejs for deployment and simple frontend-development

RUN gem install bundler rails
# rails - framework for development, bundler - is a gem ("external library") for installation gems.
# Add the application to the application path.
# make a folder, -p - make another folder inside of a new folder, /opt/app - name of the folders
ONBUILD COPY app /opt/app
ONBUILD WORKDIR /opt/app
ONBUILD EXPOSE 3000
# Default Ruby on Rails port number
ONBUILD RUN bundle install
# Run bundle install to be able to install all the necessary gems in the Gemlock file
# bundle is the same as apt-get just for ruby on rails
ONBUILD RUN rails db:migrate
ONBUILD RUN rails db:seed