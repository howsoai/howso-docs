#!/bin/sh
#
# Runs the platform documentation nginx 
#
set -eu

# Create logout page from template - since it includes ums host in redirect
cat /container_files/templates/logout.html.tmpl | envsubst | tee /usr/share/nginx/html/logout.html
cat /container_files/templates/howso.html.tmpl | envsubst | tee /usr/share/nginx/html/howso.html

nginx -g 'daemon off;'
