#!/usr/bin/env bash
docker run --rm -v hello:/world --mount type=bind,source="$(pwd)/copy_from_me",target="/copy_from_me" alpine cp -r "/copy_from_me/." /world/.
