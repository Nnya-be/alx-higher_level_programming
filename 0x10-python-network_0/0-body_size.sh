#!/usr/bin/env bash
#Writes the content of a request lenght.

url=$1
size=$(curl -sI "$url" | grep -i "Content-length' | awk '{print $2}' | tr -d '\r\n')
echo "$size"
