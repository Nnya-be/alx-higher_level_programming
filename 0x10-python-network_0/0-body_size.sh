#!/bin/bash
#Writes the content of a request lenght.
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
