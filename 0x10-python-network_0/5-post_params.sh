#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable email must be sent
email="test@gmail.com";subject="I will always be here for PLD";curl -s -X POST -d "email=$email&subject=$subject" "$1"
