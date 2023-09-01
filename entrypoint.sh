#! /usr/bin/env sh

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi


exec "$@"