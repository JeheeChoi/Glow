#!/bin/bash

curl "http://localhost:8000/boards" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "board": {
      "title": "'"${TITLE}"'",
      "topic": "'"${TOPIC}"'",
    }
  }'

echo
