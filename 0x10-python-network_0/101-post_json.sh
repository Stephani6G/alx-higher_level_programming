#!/bin/bash
# sends a JSON POST request to a URL, and displays th
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
