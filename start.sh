#!/bin/sh
gunicorn main:main --workers 15 --threads 8 --bind 0.0.0.0:80 --timeout 86400 --worker-class aiohttp.GunicornWebWorker & python3 -m bot
