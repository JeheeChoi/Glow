#!/bin/bash

curl "http://localhost:8000/glows/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "glow": {
      "message": "'"${MESSAGE}"'",
      "name": "'"${NAME}"'",
      "board_id": "'"${BOARD_ID}"'",
    }
  }'

echo
