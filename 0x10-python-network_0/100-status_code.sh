#!/bin/bash
# Script that sends a request to a URL passed
curl -so /dev/null -w "%{http_code}" "$1"
