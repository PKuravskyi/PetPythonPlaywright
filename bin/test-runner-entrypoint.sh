#!/bin/sh

chmod +x ./bin/shopping-store-linux-amd64
./bin/shopping-store-linux-amd64 > /dev/null 2>&1 &


echo 'Waiting until ShoppingStoreApp is launched...'
timeout=10
elapsed=0
until curl -s http://localhost:2221 >/dev/null; do
  sleep 0.5
  elapsed=$((elapsed + 1))
  if [ "$elapsed" -ge "$timeout" ]; then
    echo "ShoppingStoreApp did not start within $timeout seconds. Exiting..."
    exit 1
  fi
done


echo "Running playwright tests: '${*}'"
"${@}"
