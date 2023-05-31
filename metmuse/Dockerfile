# build stage
FROM node:18.16.0-alpine as deps

WORKDIR /app

# add `/node_modules/.bin` to $PATH
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH /dashboard/node_modules/.bin:$PATH


COPY package.json ./
RUN npm install

USER root

COPY public/ /app/public
COPY src/ /app/src
COPY babel.config.js /app
COPY jsconfig.json /app
COPY vue.config.js /app

CMD ["npm", "run", "serve"]