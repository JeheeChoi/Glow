#!/bin/bash

curl "http://localhost:8000/glows/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
