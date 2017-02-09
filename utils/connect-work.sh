#!/usr/bin/env bash
set -ex

# umount /tmp/ssh

sshfs -oauto_cache,reconnect,allow_other,defer_permissions,negative_vncache,noappledouble,volname=BotoProjects \
  boto-work:/home/pi/Projects /tmp/ssh

ssh -v -2 -o ExitOnForwardFailure=yes \
  -L 9999:localhost:9999 a1 cat

#ssh -v -2 -o ExitOnForwardFailure=yes \
#  -L 0.0.0.0:27017:0.0.0.0:27017 \
#  -L 0.0.0.0:6379:0.0.0.0:6379 \
#  -L 0.0.0.0:9181:0.0.0.0:9181 a1 cat

