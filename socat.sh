#!/bin/bash

socat TCP-LISTEN:9090,reuseaddr,fork SYSTEM:'tee l2r | socat - "TCP:www.google.com:443"  | tee r2l'
