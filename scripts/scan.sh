#!/usr/bin/env bash
set -euo pipefail

: "${SONAR_TOKEN:?Vous devez définir SONAR_TOKEN (token projet SonarQube)}"
: "${SONAR_HOST_URL:=http://localhost:9000}"

echo "[INFO] SONAR_HOST_URL=$SONAR_HOST_URL"

docker run --rm \
  -e SONAR_HOST_URL="$SONAR_HOST_URL" \
  -e SONAR_TOKEN="$SONAR_TOKEN" \
  -v "$(pwd):/usr/src" \
  sonarsource/sonar-scanner-cli:latest
