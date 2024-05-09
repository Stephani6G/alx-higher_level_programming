#!/bin/bash
# Makes a request to the url passed as an argument, and responds
curl -sLX PUT --post{1..3} -d "user_id=98" -H "Origin: School" "$1"
