#! /usr/bin/env sh

export $(cat .env.production | xargs)

TAG=prod bash ./scripts/build.sh

DOMAIN=api.margret.pw \
TRAEFIK_TAG=api.margret.pw \
STACK_NAME=api-margret-pw \
TAG=prod \
bash ./scripts/deploy.sh
