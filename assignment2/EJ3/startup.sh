#!/bin/sh
set -e

TARGET_DIR="/usr/share/nginx/html"

rm -rf "${TARGET_DIR:?}"/*
mkdir -p "$TARGET_DIR"
cd /tmp

wget -E -k -p "$SITE_URL"

HOST_DIR="$(echo "$SITE_URL" | sed -E 's#https?://##' | sed 's#/$##')"

if [ -d "/tmp/$HOST_DIR" ]; then
  cp -r /tmp/"$HOST_DIR"/* "$TARGET_DIR"/
fi

chmod -R 755 "$TARGET_DIR"

exec nginx -g 'daemon off;'