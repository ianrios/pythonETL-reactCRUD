#! /usr/bin/env sh

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    pip install python-dotenv
    flask run
fi

if [ -f "package.json" ]; then
    npm install
    npm start
fi

exec "$@"