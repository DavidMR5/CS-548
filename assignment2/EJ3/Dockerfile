FROM nginx:1.29.5-alpine

RUN apk add --no-cache wget ca-certificates bash

COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

ENV SITE_URL=https://www.csd.uoc.gr/

ENTRYPOINT ["/startup.sh"]