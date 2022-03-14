#! /usr/bin/env sh

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

while sleep 1000; do :; done
