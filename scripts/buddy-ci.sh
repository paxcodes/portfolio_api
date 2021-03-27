#! /usr/bin/env sh

TAG=prod bash ./scripts/build.sh

DOMAIN=api.margret.pw \
TRAEFIK_TAG=api.margret.pw \
STACK_NAME=api-margret-pw \
TAG=prod \
bash ./scripts/deploy.sh
