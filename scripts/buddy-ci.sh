#! /usr/bin/env sh

# Exit in case of error
set -e

export $(cat .env.production | sed 's/#.*//g' | xargs)

TAG=prod bash ./scripts/build.sh

DOMAIN=api.margret.pw \
TRAEFIK_TAG=api.margret.pw \
STACK_NAME=api-margret-pw \
TAG=prod \
bash ./scripts/deploy.sh
