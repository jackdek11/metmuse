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

RUN npm run build

FROM nginx:stable-alpine as production-stage

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d

COPY --from=deps /app/dist /usr/share/nginx/html

RUN nginx -t

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]