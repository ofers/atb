#!/bin/bash

sudo docker stack deploy -c atbapp.yml atbapp --with-registry-auth
