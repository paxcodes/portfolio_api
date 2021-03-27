#! /usr/bin/env sh

export $(cat .env.production | sed 's/#.*//g' | xargs)

TAG=prod \
STACK_NAME=api-margret-pw \
bash ./scripts/build.sh

DOMAIN=api.margret.pw \
TRAEFIK_TAG=api.margret.pw \
STACK_NAME=api-margret-pw \
TAG=prod \
bash ./scripts/deploy.sh
