FROM node:16.19-alpine as build-stage

RUN apk add git
RUN git clone https://github.com/Richard-mb9/toro.web.git

WORKDIR /toro.web

RUN npm install
RUN npm run build -- --output-path=./dist/out

FROM nginx:1.15

COPY --from=build-stage /toro.web/dist/out/ /usr/share/nginx/html
COPY --from=build-stage /toro.web/default.conf /etc/nginx/conf.d

EXPOSE 4200

CMD ["nginx", "-g", "daemon off;"]