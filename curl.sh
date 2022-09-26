#!/bin/bash


curl -v  -k https://localhost:9090 -H "Host:www.google.com"
#curl -v --tls-max 1.2  -k https://localhost:9090 -H "Host:www.google.com"
