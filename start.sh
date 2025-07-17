#!/bin/bash

# Start Rasa action server in background
rasa run actions &

# Start Rasa server
rasa run \
  --enable-api \
  --cors "*" \
  --debug \
  -p 5005
